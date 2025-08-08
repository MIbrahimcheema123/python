num = int(input("Enter the value:"))
print("The length of the value you gave is:",len(str(num)))
#   OR
count = 0
while num != 0:
    num = int(num) // 10
    count += 1
print("The amount of numbers are",count)