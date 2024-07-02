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
                self.satellite_count[i][j] = Satellite()
        
        for i in range(self.satellite_count):
            for j in range(self.satellite_count):
                if i == j:
                    self.distance_map[i][j] = 0
                elif i == j - 1 or i == j + 1 or i == j - self.column or i == j + self.column:
                    self.distance_map[i][j] = 50000
                else:
                    self.distance_map[i][j] = 0x3f3f3f3f