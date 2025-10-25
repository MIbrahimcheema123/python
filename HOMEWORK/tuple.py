tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)
product1 = 1
product2 = 1
for num in tuple1:
    product1 *= num
for num in tuple2:
    product2 *= num
print("The product of tuple1 values is:", product1)
print("The product of tuple2 values is:", product2)