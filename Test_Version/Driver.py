import time
import rockBlock
import logging
#import bluetooth

# -------------SatCom constants------------------
# - need port number for communicator
portID = "/dev/serial0"
# - need callback number for communicator
callback = 0

# BlueTooth socket connection
global maxXG
global maxYG
global maxZG
global maxGyroX
global maxGyroY
global maxGyroZ
global maxTemp
logging.basicConfig(filename='CrashData.log', level=logging.DEBUG)

portID = "/dev/serial0"
callback = 0

# -------- Satellite Communicator object----------
#com = rockBlock.__init__(portID, callback)

# ------function to send data from SensorArray to formatted string, then to the SatCom unit-------
def sensorEmergency(data):
    #- Message for crash with fire
    if (abs(data[0]) > 1 or abs(data[1]) > 1.5 or abs(data[2]) > 3 or abs(data[3]) > 181 or abs(data[4]) > 181 or \
        abs(data[5]) > 181) and float(data[6]) > 70:
        # - 67 characters of text. Not enough room for data. When message hits server, modify it and fill in the
        # text, regex for live testing because of 85 character message limit. Currently 89 without timestamp.
        # Probably a bool to indicate either manually generated or automatically generated messages
        output = "AutoMsg: Crash with fire! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
                 "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + str(data[7]) + \
                 " Lon: " + str(data[8]) + " Speed: " + str(data[10])
        print(output)
        logging.info(output)
        #com.sendMessage(output)
        return driverMonitor()

    # - Message for a crash without fire
    if (abs(data[0]) > 1 or abs(data[1]) > 1.5 or abs(data[2]) > 3 or abs(data[3]) > 181 or abs(data[4]) > 181 or \
        abs(data[5])) and float(data[6]) < 70:
        output = "AutoMsg: Crash! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
                 "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + str(data[7]) + \
                 " Lon: " + str(data[8]) + " Speed: " + str(data[10]) + " Temp: " + str(data[6])
        print(output)
        logging.info(output)
        #com.sendMessage(output)
        # - Message for fire alone
        return driverMonitor()

    # - Message for fire
    elif float(data[6]) > 70:
        output = "AutoMsg: Fire! Time: " + +  data[9] + " Lat: " + str(data[7]) + " Lon: " + str(data[8])
        print(output)
        logging.info(output)
        #com.sendMessage(output)
        return driverMonitor()

#--------------------Driver script--------------------------
def driverMonitor():
    # com = rockBlock.__init__(rockBlock(0, 0)) - uncomment when SatCom is installed

    # Python has an irritating import format
    from SensorArray import SensorArray
    sense = SensorArray()

    #- Loop that dictates the behavior of the entire controller
    while True:
        sense.sensorCaller()
        # if mes.listenForMessages(None):
        # send message through com, log in output file

        # if com.messageCheck():
        # send message to mobile device, log to output file

        time.sleep(0.03)


#- Initiates primary function loop
driverMonitor()
