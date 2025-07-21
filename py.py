# made my first calculator
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
print("5 - none")
option = int(input("Choose an operation:"))
result = "0"
if (option in [1,2,3,4,5]):
    num1 = float(input("Enter the first value:"))
    num2 = float(input("Enter the second value:"))
    if (option == 1):
        result = num1 + num2
    elif (option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4):
        result = num1 / num2
    elif (option == 5):
        print("ok run the code again to completely use the calculator")
    else:
        print("the result of the equation is {}".format(result))
print(result)