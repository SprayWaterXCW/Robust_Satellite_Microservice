class Satellite:
    def __init__(self, CPU_number=4, GPU_number=4, MEMORY_mb=4096, POWER_W=200, computingAbility=100, microservice_count=0):
        self.CPU_number = CPU_number
        self.GPU_number = GPU_number
        self.MEMORY_mb = MEMORY_mb
        self.POWER_W=200
        self.computingAbility = computingAbility
        self.microservice_count = microservice_count       

    def consumeCPU(self, number):
        self.CPU_number -= number
    
    def releaseCPU(self, number):
        self.CPU_number += number
    
    def consumeGPU(self, number):
        self.GPU_number -= number
    
    def releaseGPU(self, number):
        self.GPU_number += number
        
    def consumeMemory(self, number):
        self.Memory_mb -= number
    
    def releaseMemory(self, number):
        self.Memory_mb += number
    
    def consumePower(self, number):
        self.POWER_W -= number
    
    def releasePower(self, number):
        self.POWER_W += number
