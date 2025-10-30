try:
    num1,num2 = eval(input("Enter the two values seprated by a comma:"))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is a error")
except SyntaxError:
    print("The comma between the numbers is missing")
except:
    print("Wrong input")
else:
    print("No expection")
finally:
    print("This will execute no matter what")