medical_cause = input("Do you have a meical cause Y or N:")
if medical_cause == "Y":
    print("you are allowed")
else:
    attandence = int(input("Enter your attandence"))
    if attandence >= 75:
        print("you are allowed")
    else:
        print("you are not allowed")

units = float(input("Enter the amount of units consumed:"))
if units < 50:
    amt = units * 2.60
    tax = 50
elif units < 100 :
    amt = units * 3.20
    tax = 75
elif units < 200 :
    amt = units * 5.26
    tax = 150
else :
    amt = units * 8
    tax = 300
total = amt + tax
print