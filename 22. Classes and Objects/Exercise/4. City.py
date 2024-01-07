class Town:
    def __init__(self,name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"
    def set_latitude(self,latitude):
        latitude = latitude.split('\ ')
        self.latitude = ''
        for element in latitude:
            self.latitude += element
    def set_longitude(self,longitude):
        longitude = longitude.split('\ ')
        self.longitude = ''
        for element in longitude:
            self.longitude += element
    def __repr__(self):
        return f'Town: {self.name}, | Latitude: {self.latitude} | Longitude: {self.longitude}'


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
