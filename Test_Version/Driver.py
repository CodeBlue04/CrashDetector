import time

#import bluetooth

# -------------SatCom constants------------------
# - need port number for communicator
portID = 0
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


server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# - need to set up one listener for driver to check for bluetooth message
# - Contact info must be stored on email server. Message logging not necessary
# - on device, since server does all of the back end work with who to send to.
# - Provide ID from mobile app, or SOS code from device button
# Use logging library to log how many messages are sent/received, log every 5 minute location data in csv file
# look into how much data is used for data tracking

#port = 1
#server_sock.bind(("", port))
#server_sock.listen(1)

#client_sock, address = server_sock.accept()
#print("Accepted connection from ", address)

#data = client_sock.recv(1024)
#print("received [%s]" % data)

# -------- Satellite Communicator object----------
# com = rockBlock.__init__(portID, callback)

# ------function to send data from SensorArray to formatted string, then to the SatCom unit-------
def sensorEmergency(data):
    #- Message for crash with fire
    # if (abs(data[0]) > 1 or abs(data[1]) > 1.5 or abs(data[2]) > 3 or abs(data[3]) > 181 or abs(data[4]) > 181 or \
    #     abs(data[5]) > 181) and float(data[6]) > 70:
    #     # - 67 characters of text. Not enough room for data. When message hits server, modify it and fill in the
    #     # text, regex for live testing because of 85 character message limit. Curretly 89 without timestamp.
    #     # Probably a bool to indicate either manually generated or automatically generated messages
    #     output = "AutoMsg: Crash with fire! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
    #              "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + str(data[7]) + \
    #              " Lon: " + str(data[8]) + " Speed: " + str(data[10])
    #     print(output)
    #     # com.sendMessage(output)
    #     return True
    #
    # # - Message for a crash without fire
    # if (abs(data[0]) > 1 or abs(data[1]) > 1.5 or abs(data[2]) > 3 or abs(data[3]) > 181 or abs(data[4]) > 181 or \
    #     abs(data[5])) and float(data[6]) < 70:
    #     output = "AutoMsg: Crash! Time: " + data[9] + " gX: " + "%.1f" % data[0] + " gY: " + \
    #              "%.1f" % data[1] + " gZ: " + "%.1f" % data[2] + " Lat: " + str(data[7]) + \
    #              " Lon: " + str(data[8]) + " Speed: " + str(data[10]) + " Temp: " + str(data[6])
    #     print(output)
    #     # com.sendMessage(output)
    #     # - Message for fire alone
    #     return True
    #
    # # - Message for fire
    # elif float(data[6]) > 70:
    #     output = "AutoMsg: Fire! Time: " + +  data[9] + " Lat: " + str(data[7]) + " Lon: " + str(data[8])
    #     print(output)
    #     # com.sendMessage(output)
    #     return True

#TODO Getting weird index out of bounds error for speed, comment out speed and assume that temp is out of sequence. Testing in progress.
    gXMax = data[0]
    gYMax = data[1]
    gZMax= data[2]
    temperature= data[3]
    gyroXMax= data[4]
    gyroYMax= data[5]
    gyroZMax= data[6]
    lat= data[7]
    lon= data[8]
    alt= data[9]
    time= data[10]
    speed= data[11]

    output = "maxXG: " + str(gXMax) + " maxYG: " + str(gYMax) + " maxZG: " + str(
        gZMax) + " Temp: " + str(temperature) + "Gyro X" \
    + str(gyroXMax) + " Gyro Y: " + str(gyroYMax) + "Gyro Z: " + str(
        gyroZMax) + " Lat: " \
    + str(lat) + " Lon: " + str(lon) + " Alt: " + str(alt) + " Time: " + \
    str(time) + " Speed: " + str(speed)
    with open("/home/pi/Documents/output.txt", "a") as myFile:
        myFile.write(str(output))
        myFile.write("\n")


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
