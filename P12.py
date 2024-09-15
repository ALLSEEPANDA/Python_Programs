word = input("Enter a word: ")
vowels = 'aeiouAEIOU'
for vowel in vowels:
    word = word.replace(vowel, ' ')
print("New word:", word)