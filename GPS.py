from gps3 import agps3


class GPS(object):
    # - These four open a connection to the GPS receiver, create a stream to this class, and monitor the connection
    gps_socket = agps3.GPSDSocket()
    data_stream = agps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()

    # - Constructor with relevant values. It also defines the GPS data socket and data stream
    def __GPS__(self):
        #- Latitude
        self.lat = 0.0

        #- Longitude
        self.long = 0.0

        #- Speed
        self.speed = 0.0

        #- Altitude
        self.alt = 0.0

        #- Accurate time
        self.time = 0

    #- Setter. Collects data from the receiver, formats it, and updates the GPS object fields
    def setValues(self):
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                self.lat = (self.data_stream.lat)
                self.long = (self.data_stream.lon)
                self.speed = (self.data_stream.speed)
                self.alt = (self.data_stream.alt)
                self.time = (self.data_stream.time)
                return True
            else:
                return False

    # - Getters
    @property
    def getLat(self):
        return self.lat

    @property
    def getLong(self):
        return self.long

    @property
    def getSpeed(self):
        return self.speed

    @property
    def getTime(self):
        return self.time

    @property
    def getAlt(self):
        return self.alt
