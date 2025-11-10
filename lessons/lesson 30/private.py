class myclass:
    __privating = 67
    def __privatemothed(self):
        print("I am not inside myclass")
    def hi(self):
        print("This is the private variable:",myclass.__privating)
obj = myclass()
obj.hi()
obj.__privatemothed() 