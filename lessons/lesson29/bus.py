class vehicle:
    def __init__(self,name,maxspeed,milaege):
        self.name = name
        self.maxspeed = maxspeed
        self.milaege = milaege
class bus(vehicle):
    pass
power =bus("Matro",50000000000,0.00000000001)
print("vehicle",power.name)
print("maxspeed",power.maxspeed)
print("milaege",power.milaege)