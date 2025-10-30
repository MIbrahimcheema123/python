num = int(input("Enter the number:"))
def cube(num):
    return num*num*num
def hi(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
print(hi(num))