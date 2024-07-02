from request import Request
import random

class RequestGraph:
    def __init__(self, area_count, row, column, time_line):
       self.area_count = area_count
       self.row = row
       self.column = column
       self.time_line = time_line
       self.request_list = [[[] for j in range(self.row)] for i in range(time_line)]

       self.init()

    def init(self):
        for i in range(self.time_line):
            for j in range(self.row):
                for k in range(self.column):
                    self.request_list[i][j].append(Request(j * self.column + k, i, random.randint(5, 15)))