word_frequency = {'codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}
print("Dictionary:", word_frequency)
word = input("Enter the word you want to check the frequency of:")
if word in word_frequency:
    print(f"The frequency of'{word}'is{word_frequency[word]}")
else:
    print(f"'{word}'is not found in the dictionary")