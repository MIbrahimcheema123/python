weather = (1,0,0,0,1,1,0)
sunny = 0
riany = 0
for i in range(0,7):
    if weather[i] == 0:
        sunny += 1
    else:
        riany += 1
if  sunny > riany:
    print("The weather is good")
else:
    print("The weather is bad")