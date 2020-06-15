# CrashDetector
My first Raspberry Pi project. The ultimate goal is to bring together data from a BerryIMU accelerometer/gyro/pressure sensor 
(with some of that code base) and a GPS unit to detect vehicle collsions and/or fires, then send that data through the Iridium 
Satellite Network using a RockBLOCK 9603 and an external antenna to a Raspberry Pi server, which then sends messages to the user's 
predetermined contact list. 

### Current State:
In its current form the sensor array works and formats the message properly for transmission, the server code ("CoreMonitor.py") is functioning as intended, and the system is working correctly for collecting test data using the Test_Version. The Test_Version is intended to help determine the G and gyroscopic rotation limits of your normal riding or driving, including a data parsing script which helps visualize the data points you collect using the test code.

Beyond the code, I've also put up .stl files of the case I designed using Autodesk Fusion 360. These are a work in progess, but the version here is perfectly fine. I'm just making minor tweaks at this point. The primary goal of the case is obviously to house the hardware, but the next highest priority is to keep the case as small as is feasible to accommodate being mounted to a wider array of vehicles. Sportbikes, for instance, have notoriously small cargo compartments (if any) and present a series of challenges. Right now I'm able to fit this iteration into the glove box of my KTM 990 Adventure along with a battery pack to run the device. 

### Present Challenge:
At present, I've connected the RockBlock 9603 and am doing battle with I2C getting it set up for a full test run. That is the challenge I'm working through at the moment, but as soon as that's complete the client device and server will be fully functional.

### Future Plans:
The next step after testing the RockBlock is going to be an Android application which will provide messenger functionality through the satellite network.

### Additional Documentation:
The documentation (glossary, diagrams, use cases, domain model, etc.) for the project is in a constant state of change, 
but here's where it's stored and updated: 
https://docs.google.com/document/d/1mS5y7tkbaYyyo5-iuApGxk0LYctw3lzjlM7L3d9vrC4/edit?usp=sharing       

I also occasionally write about it at curiositykillscolby.com.
