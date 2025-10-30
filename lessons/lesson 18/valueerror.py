try:
    num = int(input("Enter the value:e"))
    print("The number is",num)
except ValueError as v:
    print("Exeption is",v)
