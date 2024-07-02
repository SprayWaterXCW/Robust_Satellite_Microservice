from request_graph import RequestGraph
from satellite_graph import SatelliteGraph
import random

class Env:
    def __init__(self, satellite_count, row, column, area_count, time_line):
        self.requestGraph = RequestGraph(area_count, row, column, time_line)
        self.satelliteGraph = SatelliteGraph(satellite_count, row, column)
        self.lightMicroserviceCostList = [random.randint(1, 4), random.randint(0, 4), random.randint(1, 4096), random.randint(1, 200)]