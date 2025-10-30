valid = False
while not valid:
    try:
        n = int(input("Enter a number:"))
        while n%2 == 0:
            print("I am better than my brother")
        valid = True
    except ValueError:
        print("Invalid value")