class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+"("+self.meaning+")"
flash = []
print("welcome to flash card aplication")
while True:
    word = input("Enter the word:")
    meaning = input("Enter the meaning:")
    flash.append(flashcards(word,meaning))
    option = int(input("Enter 0 if you want to continue else enter 1:"))
    if option:
        break
print("your flash cards")
for i in flash:
    print(">",i)