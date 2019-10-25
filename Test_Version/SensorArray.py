import IMUSensors
from GPS import GPS


class SensorArray:
    # - Opens GPSD socket and starts collecting data, also useful in alertDriver function
    gps = GPS()

    #- Takes data from IMUSensors, collects GPS data from GPS class, then sends it to the Driver for messaging
    def alertDriver(self, data):
        import Driver
        output = data
        output.append(self.gps.lat)
        output.append(self.gps.long)
        output.append(self.gps.time)
        output.append(self.gps.speed)
        Driver.sensorEmergency(output)

    #- Called by Driver to update IMUSensors and GPS data constantly
    def sensorCaller(self):
        acc = IMUSensors.IMUSensors()
        self.gps.setValues()
        acc.updateValues()
        return True
