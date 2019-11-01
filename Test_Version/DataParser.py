import numpy as n #to use min/max/average functions

#TODO: Before using this script, all descriptors (strings) must be removed from test data, to do this just go into any text
# editor and use the "find and replace" function to replace every descriptor string with ''


filepath = "TestData.txt"

#Open test data text file and count the lines, not required, but useful
with open(filepath) as f:
   count = sum(1 for _ in f)
print(count)

#initialize lists for each category of data
testdata = []
XGarr = []
YGarr = []
ZGarr = []
GyroXarr = []
GyroYarr = []
GyroZarr = []
latarr = []
lonarr = []
timearr = []
speedarr = []
unknownarr = []

#Loop to cycle through test data
with open(filepath) as fp:
    for line in fp:
        token = line.replace(' ', '')
        testdata = token.split(',')
        XGarr.append(float(testdata[0]))
        YGarr.append(float(testdata[1]))
        ZGarr.append(float(testdata[2]))
        GyroXarr.append(float(testdata[3]))
        GyroYarr.append(float(testdata[4]))
        GyroZarr.append(float(testdata[5]))
        latarr.append(testdata[6])
        lonarr.append(testdata[7])
        timearr.append(testdata[8])
        speedarr.append(testdata[9])
        unknownarr.append(testdata[10])

#Print low, high, and average values to console. Averages should be in the 0 range for everything but the Z axis G,
# which will hover near -1 G
print("Max X G: " + str(n.max(XGarr)))
print("Max Y G: " + str(n.max(YGarr)))
print("Max Z G: " + str(n.max(ZGarr)))
print("Max X Gyro: " + str(n.max(GyroXarr)))
print("Max Y Gyro: " + str(n.max(GyroYarr)))
print("Max Z Gyro: " + str(n.max(GyroZarr)))
print("Min X G: " + str(n.min(XGarr)))
print("Min Y G: " + str(n.min(YGarr)))
print("Min Z G: " + str(n.min(ZGarr)))
print("Min X Gyro: " + str(n.min(GyroXarr)))
print("Min Y Gyro: " + str(n.min(GyroYarr)))
print("Min Z Gyro: " + str(n.min(GyroZarr)))
print("Avg X G: " + str(n.mean(XGarr)))
print("Avg Y G: " + str(n.mean(YGarr)))
print("Avg Z G: " + str(n.mean(ZGarr)))
print("Avg X Gyro: " + str(n.mean(GyroXarr)))
print("Avg Y Gyro: " + str(n.mean(GyroYarr)))
print("Avg Z Gyro: " + str(n.mean(GyroZarr)))
