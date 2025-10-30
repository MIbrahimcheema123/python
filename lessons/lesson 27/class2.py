class parrot:
    spieces = "bird"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
p1 = parrot("palani",1000)
p2 = parrot("paroo",100000000000000000000000000000000000000000000000000000000000000000000)
print(p1.name,"is a",p1.spieces,"and it is",p1.age,"years old")
print(p2.name,"is a",p2.spieces,"and it is",p2.age,"years old")