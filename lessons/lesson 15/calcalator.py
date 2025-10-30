def add(q,p):
    return q+p
def subtract(q,p):
    return q-p
def multiply(q,p):
    return q*p
def divide(q,p):
    return q/p
print("choose an opration")
print("a = add")
print("b = subtract")
print("c = multiply")
print("d = divide")
choice = input("Enter the opperation:")
num1 = float(input("Enter first value:"))
num2 = float(input("Enter second value:"))
if choice == "a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == "b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == "c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == "d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid operation added")