name = input("Enter the name:")
for i in name:
    if i == "a"or i == "A":
        print("a or A was found")
        break
    else:
        print("a or A was not found")