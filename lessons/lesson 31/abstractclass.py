from abc import ABC,abstractmethod
class clock(ABC):
    def print(self,x):
        print("the value of x is",x)
    @abstractmethod
    def task(self):
        print("i am inside clock class")
class chair(clock):
    def task(self):
        print("i am inside chair class")
bottle_obj = chair()
bottle_obj.task()
bottle_obj.print(1234567890)