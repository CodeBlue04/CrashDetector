# CrashDetector
My first Raspberry Pi project. The ultimate goal is to bring together data from a BerryIMU accelerometer/gyro/pressure sensor 
(with some of that code base) and a GPS unit to detect vehicle collsions and/or fires, then send that data through the Iridium 
Satellite Network using a RockBLOCK 9603 and an external antenna to a server, which will then send messages to the user's 
predetermined contact list. 

In its current form the sensor array works and formats the message properly for transmission, the server code ("CoreMonitor.py") is functioning as intended, and the system is working correctly for collecting test data using the Test_Version. The Test_Version is intended to help determine the G and gyroscopic rotation limits of your normal riding, including a data parsing script which helps visualize the data points you collect using the test code.

Beyond the code, I've also put up .stl files of the case I designed using Autodesk Fusion 360. These are a work in progess, but the version here is perfectly fine. I'm just making minor tweaks at this point.

At present, I've connected the RockBlodk 9603 and am beginning to test the pyRockBlock library with my code. There should be updates within the next couple of weeks as I'm trying to finish the non-mobile app side of this project, release my first commercial program, study for finals, prepare a presentation and write a report about starting my company, and build a file system for my Operating Systems class. Things are hectic, but this is a high priority considering I had to ride home in the snow two days ago and would like to have this device up and running in those conditions.

The documentation (glossary, diagrams, use cases, domain model, etc.) for the project is in a constant state of change, 
but here's where it's stored and updated: 
https://docs.google.com/document/d/1mS5y7tkbaYyyo5-iuApGxk0LYctw3lzjlM7L3d9vrC4/edit?usp=sharing       

I also occasionally write about it at curiositykillscolby.com.
