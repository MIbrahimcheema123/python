import math
print("option1: sin")
print("option2: cos")
print("option3: tan")
option = input("Enter what you want to do:")
value = input("Enter the value:")
if option == "cos":
    print("Your value in",option,"will be",math.cos*value)
if option == "sin":
    print("Your value in",option,"will be",math.sin*value)
if option == "tan":
    print("Your value in",option,"will be",math.tan*value)