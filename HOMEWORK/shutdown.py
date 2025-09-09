hi = str(input("Do you wanna shutdown this program:"))
def shutdown():
    if hi == "yes":
        print("Shuting down")
    elif hi == "no":
        print("Abort shut down")
    else:
        print("sorry")
shutdown()