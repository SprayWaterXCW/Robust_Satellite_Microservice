from request_graph import RequestGraph
from satellite_graph import SatelliteGraph
import random
import pickle

class Env:
    def __init__(self, satellite_count=8, row=2, column=4, area_count=8, time_line=100, lightMicroserviceCount=1, heavyMicroserviceCount=2):
        # 请求图
        self.requestGraph = RequestGraph(area_count, row, column, time_line)
        # 卫星图，网状
        self.satelliteGraph = SatelliteGraph(satellite_count, row, column)
        # 距离常数
        self.distanceConstant = 50000 #km
        # 传输速度
        self.transimitionSpeed = 10.0 #Mb
        # 传播速度，光速
        self.propagationSpeed = 300000.0 #km
        # 轻量微服务数，默认为1
        self.lightMicroserviceCount = lightMicroserviceCount
        # 核心微服务数，默认为2
        self.heavyMicroserviceCount = heavyMicroserviceCount
        # 轻量微服务资源消耗
        self.lightMicroserviceCostList = [random.randint(1, 4), random.randint(0, 4), random.randint(1, 4096), random.randint(1, 200)] #CPU, GPU, Memory, Power
        # 轻量微服务计算复杂度
        self.lightMicroserviceComputingCountList = [random.randint(1, 10000) for i in range(self.lightMicroserviceCount)]
        # 轻量微服务计算结果大小
        self.lightMicroserviceResultCostList = [random.randint(1, 1000) for i in range(self.lightMicroserviceCount)]
        # 核心微服务资源消耗
        self.heavyMicroserviceCostList = [[random.randint(1, 4), random.randint(0, 4), random.randint(1, 4096), random.randint(1, 200)] for i in range(self.heavyMicroserviceCount)]
        # 核心微服务部署位置
        self.heavyMicroserviceDeploymentPositionList = [random.randint(0, self.satelliteGraph.satellite_count - 1) for i in range(self.heavyMicroserviceCount)]
        # 核心微服务计算复杂度
        self.heavyMicroserviceComputingCountList = [random.randint(1, 10000) for i in range(self.heavyMicroserviceCount)]
        # 核心微服务计算结果大小
        self.heavyMicroserviceResultCostList = [random.randint(1, 1000) for i in range(self.heavyMicroserviceCount)]
    
    def getSatelliteID(self, x, y):
        return x * self.satelliteGraph.column + y
    
    def getSatelliteXY(self, ID):
        x = 0
        y = 0
        while(ID >= self.satelliteGraph.column):
            ID -= self.satelliteGraph.column
            x += 1
        y = ID

        return x, y
    
    def getDistance(self, ID_a, ID_b):
        x_a, y_a = self.getSatelliteXY(ID_a)
        x_b, y_b = self.getSatelliteXY(ID_b)

        return self.distanceConstant * (abs(x_a - x_b) + abs(y_a - y_b))
    
    def getTransmissionLatency(self, microserviceID, microserviceType, satelliteA, satelliteB):
        x_a, y_a = self.getSatelliteXY(satelliteA)
        x_b, y_b = self.getSatelliteXY(satelliteB)
        oneTransmissionLatency = 0
        if microserviceType == 0: #light
            oneTransmissionLatency = self.lightMicroserviceCostList[microserviceID] / self.transimitionSpeed
        else:
            oneTransmissionLatency = self.heavyMicroserviceCostList[microserviceID] / self.transimitionSpeed

        return oneTransmissionLatency * (abs(x_a - x_b) + abs(y_a - y_b))
    
    def getPropagationLatency(self, satelliteA, satelliteB):
        distance = self.getDistance(satelliteA, satelliteB)

        return distance / self.propagationSpeed
    
    def getComputingLatency(self, microserviceID, microserviceType, satelliteID):
        x, y = self.getSatelliteXY(satelliteID)
        computingCount = 0
        if microserviceType == 0:
            computingCount = self.lightMicroserviceComputingCountList[microserviceID]
        else:
            computingCount = self.heavyMicroserviceComputingCountList[microserviceID]

        return computingCount / (self.satelliteGraph.satellite_map[x][y].computingAbility * 1.0)
    
if __name__ == "__main__":
    env = Env()
    output = open("../data/env.pkl", "wb")
    output.write(pickle.dumps(env))
    output.close()

    env2 = Env()
    with open("../data/env.pkl", "rb") as file:
        env2 = pickle.loads(file.read())
    
    print(pickle.dumps(env) == pickle.dumps(env2))
    print(1)