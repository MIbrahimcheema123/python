import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","banana":"yellow","kiwi":"brown","orange":"orange"}
    def quiz(self):
        while True:
            fruit,colour = random.choice(list(self.fruits.items()))
            print("What is the colour of",fruit,":")
            answer = input()
            if answer.lower()==colour:
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("Enter 0 if you want to continue else enter 1:"))
            if option:
                break
print("welcome ton fruit quiz")
obj = fruitquiz()
obj.quiz()