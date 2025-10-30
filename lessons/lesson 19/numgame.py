import random
playing = True
num = random.randint(0,1)
print("I will genrate a number from 0 to 20 guess thr number or you are bad at online games just see your careear is line so guess it correctly")
while playing:
    guess = int(input("Enter your guess:"))
    if guess == num:
        print("By a chance in 1 by 20 you saved your respect and can go freely")
        print("So the number that saved your whole gaming career was",num)
        break
    else:
        print("Shahir and muki I fianlly proved that I am better than you just ggs than")