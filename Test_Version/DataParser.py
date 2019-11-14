import numpy as n
import matplotlib.pyplot as plt

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
        XGarr.append(round(float(testdata[0]), 2))
        YGarr.append(round(float(testdata[1]), 2))
        ZGarr.append(round(float(testdata[2]), 2))
        GyroXarr.append(round(float(testdata[3]), 2))
        GyroYarr.append(round(float(testdata[4]), 2))
        GyroZarr.append(round(float(testdata[5]), 2))
        latarr.append(testdata[6])
        lonarr.append(testdata[7])
        timearr.append(testdata[8])
        speedarr.append(testdata[9])
        unknownarr.append(testdata[10])

#Print low, high, and average values to console. Averages should be in the 0 range for everything but the Z axis G,
# which will hover near -1 G
print("Max X G: " + str(round(n.max(XGarr), 2)))
print("Max Y G: " + str(round(n.max(YGarr), 2)))
print("Max Z G: " + str(round(n.max(ZGarr), 2)))
print("Max X Gyro: " + str(round(n.max(GyroXarr), 2)))
print("Max Y Gyro: " + str(round(n.max(GyroYarr), 2)))
print("Max Z Gyro: " + str(round(n.max(GyroZarr), 2)))
print("Min X G: " + str(round(n.min(XGarr), 2)))
print("Min Y G: " + str(round(n.min(YGarr), 2)))
print("Min Z G: " + str(round(n.min(ZGarr), 2)))
print("Min X Gyro: " + str(round(n.min(GyroXarr), 2)))
print("Min Y Gyro: " + str(round(n.min(GyroYarr), 2)))
print("Min Z Gyro: " + str(round(n.min(GyroZarr), 2)))
print("Avg X G: " + str(round(n.mean(XGarr), 2)))
print("Avg Y G: " + str(round(n.mean(YGarr), 2)))
print("Avg Z G: " + str(round(n.mean(ZGarr), 2)))
print("Avg X Gyro: " + str(round(n.mean(GyroXarr), 2)))
print("Avg Y Gyro: " + str(round(n.mean(GyroYarr), 2)))
print("Avg Z Gyro: " + str(round(n.mean(GyroZarr), 2)))


fig, axs = plt.subplots(3, 2)
axs[0, 0].hist(XGarr, bins=200)
axs[0, 0].set_title('X G')
axs[0, 0].set(xlabel='Frequency', ylabel='Lateral G')
axs[0, 1].hist(YGarr, bins=200)
axs[0, 1].set_title('Y G')
axs[0, 1].set(xlabel='Frequency', ylabel='Accel/Decel G')
axs[1, 0].hist(ZGarr, bins=200)
axs[1, 0].set_title('Z G')
axs[1, 0].set(xlabel='Frequency', ylabel='Vertical G')
axs[1, 1].hist(GyroXarr, bins=500)
axs[1, 1].set_title('X Gyro')
axs[1, 1].set(xlabel='Frequency', ylabel='Lateral Degree Change')
axs[2, 0].hist(GyroYarr, bins=500)
axs[2, 0].set_title('Y Gyro')
axs[2, 0].set(xlabel='Frequency', ylabel='Accel/Decel Degree Change')
axs[2, 1].hist(GyroZarr, bins=500)
axs[2, 1].set_title('Z Gyro')
axs[2, 1].set(xlabel='Frequency', ylabel='Vertical Degree Change')

plt.show()
