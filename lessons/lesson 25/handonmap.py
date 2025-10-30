num1 = [12,32,45]
num2 = [34,67,43]
result = map(lambda x,y:x+y,num1,num2)
print(list(result))

num3 = [23,435,4546]
def sq(n):
    return n*n
resultt = list(map(sq,num3))
print(resultt)