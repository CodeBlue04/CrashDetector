import time
import rockBlock
import logging

# -------------SatCom constants------------------
# - Port number for communicator
portID = "/dev/ttyUSB0"
# - Callback number for communicator
callback = 0

# -----------------Logging------------------------
logging.basicConfig(filename='CrashData.log', level=logging.DEBUG)

# -------- Satellite Communicator object----------
com = rockBlock.__init__(portID, callback)

# ------Function to send data from SensorArray to formatted string, then to the SatCom unit-------
def sensorEmergency(data):
    #- Message for crash with fire
    if data[0] > 1 or data[1] > 1.5 or data[2] > 3 and data[6] > 80:
        output = "Crash+Fire! Time:" + data[9] + " gX:" + "%.1f" % data[0] + " gY:" + \
                 "%.1f" % data[1] + " gZ:" + "%.1f" % data[2] + " Lat:" + "%.4f" % data[7] + \
                 " Lon:" + "%.4f" % data[8] + " Speed:" + "%.0f" % data[10]
        #print(output)
        logging.info(output)
        com.sendMessage(output)
        return True

    # - Message for a crash without fire
    if data[0] > 1 or data[1] > 1.5 or data[2] > 3 and data[6] < 80:
        output = "Crash! Time:" + data[9] + " gX:" + "%.1f" % data[0] + " gY:" + \
                 "%.1f" % data[1] + " gZ:" + "%.1f" % data[2] + " Lat:" + "%.4f" % data[7] + \
                 " Lon:" + "%.4f" % data[8] + " Speed:" + "%.0f" % data[10]
        #print(output)
        logging.info(output)
        com.sendMessage(output)
        return True

    # - Message for fire
    elif data[6] > 80:
        output = "Fire! Time: " + +  data[9] + " Lat:" + "%.4f" % data[7] + " Lon:" + "%.4f"\
                 % data[8]
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
        #- Get updated sensor values
        sense.sensorCaller()

        #- Delay to make output more stable
        time.sleep(0.03)


#- Initiates primary function loop
driverMonitor()
