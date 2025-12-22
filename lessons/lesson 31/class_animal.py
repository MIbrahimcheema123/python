from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk , swim and run")
class bird(animal):
    def move(self):
        print("I can fly")
class shark(animal):
    def move(self):
        print("I can swim alot faster than humans")
class leapord(animal):
    def move(self):
        print("I can run alot faster than humans")
class lion(animal):
    def move(self):
        print("I am king of the jungle")
a = human()
a.move()
b = bird()
b.move()
c = shark()
c.move()
d = leapord()
d.move()
e = lion()
e.move()