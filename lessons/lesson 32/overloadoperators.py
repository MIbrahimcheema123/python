class X:
    def __init__(self,x):
        self.x = x
    def __lt__(self,other):
        if self.x<other.x:
            return "the first num is less than the sec num"
        else:
            return "the sec num is less than the first num"
    def __eq__(self,other):
        if self.x==other.x:
            return "both are equal"
        else:
            return "both are not equal"
obj0 = X(4)
obj1 = X(8)
print(obj0<obj1)
print(obj0==obj1)