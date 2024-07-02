class Request:
    def __init__(self, area=0, time=0, request_count=0):
        self.area = area
        self.time = time
        self.request_count = request_count

    def changeRequestCount(self, count):
        self.request_count += count