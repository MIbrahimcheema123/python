import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}}|:|'/.,<>?;[]]=-"
password = ""
length = int(input(print("Enter the length:")))
for a in range(length):
    password+=random.choice(characters)
print(password)