import random
option = ["rock","paper","scissor"]
user_choice = input("Enter the weapon you wanna choose:")
computer_choice = random.choice(option)
print("your choice was",user_choice)
print("computer choice was",computer_choice)
if computer_choice == user_choice:
    print("It's a tie")
elif user_choice == "rock" and computer_choice == "scissor":
    print("You won ggs man for winning")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won ggs man for winning")
elif user_choice == "scissor" and computer_choice == "paper":
    print("You won ggs man for winning")
else:
    print("Ggs man but you lose the computer won")