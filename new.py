a = input("enter the value of a:")
print(a[::-1])
print(a.upper())
# different types in python
A = input("enter the value of A:")
B = input("enter the value of B:")
C = input("enter the value of C:")
D = input("enter the value of D:")
print("type of A",type(A))
print("type of B",type(B))
print("type of C",type(C))
print("type of D",type(D))
# type casting
A =bool(A)
print("data type of B is",type(A))
B =float(B)
print("data type of B is",type(B))
C =int(C)
print("data type of C is",type(C))
D =str(D)
print("data type of D is",type(D))
# finding the average of tree length
tree1 = int(input("enter the length of tree1:"))
tree2 = int(input("enter the length of tree2:"))
tree3 = int(input("enter the length of tree3:"))
tree4 = int(input("enter the length of tree4:"))
tree5 = int(input("enter the length of tree5:"))
sum = tree1+tree2+tree3+tree4+tree5
# now we will do the multiplication
average = sum/5
print("the age of these 4 trees is:",average)
# this program will tell you how many different types of notes you have
amount = int(input("enter the amount of money you want to widraw:"))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print("notes of 100 rupee:",note_1)
print("notes of 50 rupee:",note_2)
print("notes of 10 rupee:",note_3)
#program that  tells you which close to wear so you wont get cold
tem = int(input("enter the temperatue of taday:"))
if tem > 40 :
    print("wear super light  cloths")
elif tem < 20 :
    print("wear warm cloths")
else :
    print("system error")
