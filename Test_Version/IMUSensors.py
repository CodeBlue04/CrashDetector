import datetime
import math
from ctypes import c_short
from time import sleep

from smbus import SMBus

import IMU
import SensorArray


class IMUSensors:
    # Accelerometer:
    IMU.detectIMU()  # Detect if BerryIMUv1 or BerryIMUv2 is connected.
    IMU.initIMU()  # Initialise the accelerometer, gyroscope and compass

    # Gyro
    RAD_TO_DEG = 57.29578
    M_PI = 3.14159265358979323846
    G_GAIN = 0.070  # [deg/s/LSB]  If you change the dps for gyro, you need to update this value accordingly
    AA = 0.40  # Complementary filter constant

    gyroXangle = 0.0
    gyroYangle = 0.0
    gyroZangle = 0.0

    a = datetime.datetime.now()

    # Thermometer:
    addr = 0x77
    oversampling = 3  # 0..3

    bus = SMBus(1)  # 0 for R-Pi Rev. 1, 1 for Rev. 2

    # return two bytes from data as a signed 16-bit value
    def get_short(self, data, index):
        return c_short((data[index] << 8) + data[index + 1]).value

    # return two bytes from data as an unsigned 16-bit value
    def get_ushort(self, data, index):
        return (data[index] << 8) + data[index + 1]

    # calls SensorArray class and passes array of sensor data if crash or fire detected in undateValues()
    def sensorCaller(self, dataArray):
        sense = SensorArray.SensorArray()
        sense.alertDriver(dataArray)

    #One function to rule them all. Or at least supply the bulk of sensor data.
    def updateValues(self):
        #--------------------Accelerometer sensor calculations-----------------------
        # Read the accelerometer,gyroscope and magnetometer values
        ACCx = IMU.readACCx()
        ACCy = IMU.readACCy()
        ACCz = IMU.readACCz()

        xG = (ACCx * 0.244) / 1000
        yG = (ACCy * 0.244) / 1000
        zG = (ACCz * 0.244) / 1000

        #-----------------Gyroscope sensor calculations-------------------------
        GYRx = IMU.readGYRx()
        GYRy = IMU.readGYRy()
        GYRz = IMU.readGYRz()

        ##Calculate loop Period(LP). How long between Gyro Reads
        b = datetime.datetime.now() - self.a
        self.a = datetime.datetime.now()
        LP = b.microseconds / (1000000 * 1.0)

        # Convert Gyro raw to degrees per second
        rate_gyr_x = GYRx * self.G_GAIN
        rate_gyr_y = GYRy * self.G_GAIN
        rate_gyr_z = GYRz * self.G_GAIN

        # Calculate the angles from the gyro.
        self.gyroXangle += rate_gyr_x * LP
        self.gyroYangle += rate_gyr_y * LP
        self.gyroZangle += rate_gyr_z * LP

        # Convert Accelerometer values to degrees
        self.AccXangle = (math.atan2(ACCy, ACCz) * self.RAD_TO_DEG)
        self.AccYangle = (math.atan2(ACCz, ACCx) + self.M_PI) * self.RAD_TO_DEG

        # convert the values to -180 and +180
        if self.AccYangle > 90:
            self.AccYangle -= 270.0
        else:
            self.AccYangle += 90.0

        #-------------------Thermometer calculations--------------------

        # Read whole calibration EEPROM data
        cal = self.bus.read_i2c_block_data(self.addr, 0xAA, 22)

        # Convert byte data to word values
        ac5 = self.get_ushort(cal, 8)
        ac6 = self.get_ushort(cal, 10)
        mc = self.get_short(cal, 18)
        md = self.get_short(cal, 20)

        self.bus.write_byte_data(self.addr, 0xF4, 0x2E)
        sleep(0.005)
        (msb, lsb) = self.bus.read_i2c_block_data(self.addr, 0xF6, 2)
        ut = (msb << 8) + lsb

        x1 = ((ut - ac6) * ac5) >> 15
        x2 = (mc << 11) / (x1 + md)
        b5 = x1 + x2
        t = (b5 + 8) >> 4

        temperature = t / 10.0

        #-------------------Crash condition checker-----------------------
        if abs(xG) > 1 or abs(yG) > .75 or abs(zG+1) > 1.8:
            #- creates list of data to send up to the SensorArray class
            sensorData = [xG, yG, zG, self.gyroXangle, self.gyroYangle, self.gyroZangle, str(temperature)]
            #- Sends data to SensorArray
            self.sensorCaller(sensorData)
