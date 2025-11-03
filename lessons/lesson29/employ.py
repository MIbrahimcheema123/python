class person:
    def __init__(self,name,idnum):
        self.name = name
        self.idnum = idnum
    def display(self):
        print(self.name)
        print(self.idnum)
class employ(person):
    def __init__(self,name,idnum,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,idnum)
    def print(self):
        print(self.salary)
        print(self.post)
go = employ("notgoodemploy",100000000000000000000,0,"window_cleaner")
go.display()
go.print()