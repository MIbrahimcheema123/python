print("This program wil make a diomand patteren")
rowsize =int(input("Enter the rowsize:"))
if rowsize%2 == 0:
    halfdiomandrow = int(rowsize/2)
else:
    halfdiomandrow = int(rowsize/2)+1
space = halfdiomandrow - 1
for i in range(1,halfdiomandrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space -= 1
    num  = 1
    for j in range(2*i-1):
        print(end=str(num))
        num += 1
    print()
space = 1
for i in range(1,halfdiomandrow):
    for j in range(1,space+1):
        print(end=" ")
    space += 1
    num = 1
    for j in range(1,2*(halfdiomandrow-i)):
        print(end=str(num))
        num += 1
    print()