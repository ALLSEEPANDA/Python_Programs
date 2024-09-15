word = input("Enter a word: ")
new_word = ''
for char in word:
    if char in 'aeiouAEIOU':
        new_word += ' '
    else:
        new_word += char
print("New word:", new_word)