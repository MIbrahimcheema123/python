num = int(input("Enter the value:"))
alphabet = ""
while num > 0:
    count = num%2
    print(alphabet)
    alphabet = str(count) + alphabet
    num = num//2
print(alphabet)