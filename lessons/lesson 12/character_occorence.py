string = input("Enter a string:")
character = input("Enter the character:")
i = 0
count = 0
while i<len(string):
    if string[i] == character:
        count += 1
    i += 1
print("the number of times the is repeated is:",count)