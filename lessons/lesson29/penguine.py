class bird:
    def __init__(self):
        print("Bird can be ready in a min")
    def whoisthis(self):
        print("A small bird")
    def swim(self):
        print("Can you swim faster?")
class birdy(bird):
    def __init__(self):
        super().__init__()
        print("This is a birdy")
    def whoisthis(self):
        print("Is this a good birdy")
    def run(self):
        print("Can you even swim?")
ob = birdy()
ob.whoisthis()
ob.swim()
ob.run()