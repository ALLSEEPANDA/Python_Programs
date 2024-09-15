print("Count Of Vowels In A Word")
word = input("Enter A Word : ")
count = 0

for char in word:
    if char in 'aeiouAEIOU':
        count += 1

print("Count of vowels : ",count)