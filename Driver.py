import time
import rockBlock
import logging

# -------------SatCom constants------------------
# - need port number for communicator
portID = "/dev/ttyUSB0" #Thelocation of the connection. In the libraries I'm seeing it's "/dev/ttyUSB0", but need to check since it's GPIO instead of USB
# - need callback number for communicator
callback = 0 # None apparently works?

# -----------------Logging------------------------

logging.basicConfig(filename='CrashData.log', level=logging.DEBUG)



# -------- Satellite Communicator object----------
com = rockBlock.__init__(portID, callback)

# ------function to send data from SensorArray to formatted string, then to the SatCom unit-------
def sensorEmergency(data):
    #- Message for crash with fire
    if data[0] > 1 or data[1] > 1.5 or data[2] > 3 and data[6] > 80:
        # - 67 characters of text. Not enough room for data. When message hits server, modify it and fill in the
        # text, regex for live testing because of 85 character message limit. Curretly 89 without timestamp.
        # Probably a bool to indicate either manually generated or automatically generated messages
        output = "AutoMsg: Crash with fire! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
                 "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + data[7] + \
                 " Lon: " + data[8] + " Speed: " + data[10]
        #print(output)
        logging.info(output)
        com.sendMessage(output)
        return True

    # - Message for a crash without fire
    if data[0] > 1 or data[1] > 1.5 or data[2] > 3 and data[6] < 80:
        output = "AutoMsg: Crash! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
                 "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + data[7] + \
                 " Lon: " + data[8] + " Speed: " + data[10]
        #print(output)
        logging.info(output)
        com.sendMessage(output)
        # - Message for fire alone
        return True

    # - Message for fire
    elif data[6] > 80:
        output = "AutoMsg: Fire! Time: " + +  data[9] + " Lat: " + "%.4f" % data[
            7] + " Lon: " + "%.4f" % \
                 data[8]
        #print(output)
        logging.info(output)
        com.sendMessage(output)
        return True


#--------------------Driver script--------------------------
def driverMonitor():
   # com = rockBlock.__init__(rockBlock(0, 0))

    from SensorArray import SensorArray
    sense = SensorArray()

    #- Loop that dictates the behavior of the entire controller
    while True:
        sense.sensorCaller()
        # if mes.listenForMessages(None):
        # send message through com, log in output file in future update

        # com.messageCheck():
        # send message to mobile device, log to output file in future update

        #- Delay to make output more legible
        time.sleep(0.03)


#- Initiates primary function loop
driverMonitor()
