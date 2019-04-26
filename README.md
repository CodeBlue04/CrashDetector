# CrashDetector
My first Raspberry Pi project. The ultimate goal is to bring together data from a BerryIMU accelerometer/gyro/pressure sensor 
and a GPS unit to detect vehicle collsions and/or fires, then send that data through the Iridium Satellite Network using a 
RockBLOCK mk2 and an external antenna to a server, which will then send messages to the user's predetermined contact list. 
Once the automated part is complete, I'll be building a mobile app to augment the system, but that comes after the server, I think. 
Right now the sensor array works and formats the message properly for transmission. The format will almost certainly change when 
the server is being worked on to minimize the amount of data transmitted. Next up will be the RockBLOCK, antenna, and 3d printed 
case, the code for which will all be available here. Once that's done, I'll start in on the mobile app and server. 

The documentation (glossary, diagrams, use cases, domain model, etc.) for the project is in a constant state of change, 
but here's where it's stored and updated: 
https://docs.google.com/document/d/1mS5y7tkbaYyyo5-iuApGxk0LYctw3lzjlM7L3d9vrC4/edit?usp=sharing       

I also occasionally write about it at curiositykillscolby.com.
