class employ:
    def __init__(self):
        print("Employ has entered the world")
    def __del__(self):
        print("Should destructor be called")
def dontcreateobject():
    print("making object")
    o = employ()
    print("Function end")
    return o
print("calling dontcreateobject function")
ob = dontcreateobject()
print("Should we end this program :D")