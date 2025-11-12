set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))
sym_diff = set1.symmetric_difference(set2)
print("The symmetric difference of the two sets is:", sym_diff)