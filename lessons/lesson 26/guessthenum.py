import random
import time
number = random.randint(1,50)
def intro():
    print("May i ask your name?")
    global name
    name = input()
    print(name,"we will play a small game in it i will think between a number 1 to 50")
    if number%2 == 0:
        x = "even"
    else:
        x = "odd"
    print("\n this is a",x,"number")
    time.sleep(2)
    print("go ahead and guess the number!")
def pick():
    guesstaken = 0
    while guesstaken<8:
        time.sleep(1)
        enter = input("GO guess it:")
        try:
            guess = int(enter)
            if guess <= 50 and guess >= 1:
                guesstaken += 1
                if guesstaken < 8:
                    if guess<number:
                        print ("Your guess was low")
                    if guess>number:
                        print("Your guess is higher than the number")
                    if guess != number:
                        time.sleep(1)
                        print("Try again")
                    if guess == number:
                        break
            if guess > 50 or guess < 1:
                print("Your number is not in the range")
        except:
            print("I dont think that the input you have give to me is a number")
    if guess == number:
        guesstaken = str(guesstaken)
        print("Good job",name,"you guessed my number in",guesstaken,"guess")
    if guess != number:
        print("Nope the number i was thinking was",str(number))
playagain = "yes"
while playagain == "yes" or playagain == "yea" or playagain == "yeah" or playagain == "sure" or playagain == "yup" or playagain == "Ofcourse":
    intro()
    pick()
    print ("Do you want to play again?")
    playagain = input()