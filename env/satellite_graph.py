from satellite import Satellite

class SatelliteGraph:
    def __init__(self, satellite_count, row, column):
        self.satellite_count = satellite_count
        self.row = row
        self.column = column
        self.satellite_map = [[] for i in range(self.row)]
        self.distance_map = [[] for i in range(self.satellite_count)]

        self.init()

    def init(self):
        for i in range(self.row):
            for j in range(self.column):
                self.satellite_map[i].append(Satellite())
        
        for i in range(self.satellite_count):
            for j in range(self.satellite_count):
                if i == j:
                    self.distance_map[i].append(0)
                elif self.checkSatelliteID(i, j):
                    self.distance_map[i].append(50000)
                else:
                    self.distance_map[i].append(0x3f3f3f3f)

    def checkSatelliteID(self, i, j):
        if i == j - 1 and j - 1 >= 0:
            return True
        elif i == j + 1 and j + 1 < self.satellite_count:
            return True
        elif i == j - self.column and j - self.column >= 0:
            return True
        elif i == j + self.column and j + self.column < self.satellite_count:
            return True
        else:
            return False