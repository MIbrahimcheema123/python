test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("original dictionar",str(test_dict))
value = 2
count = 0
for key in test_dict:
    if test_dict[key] == value:
        count += 1
print(count)