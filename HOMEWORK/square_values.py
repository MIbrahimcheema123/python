start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range:"))
squares = [num ** 2 for num in range(start, end + 1)]
even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]
print("\nAll squares:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)