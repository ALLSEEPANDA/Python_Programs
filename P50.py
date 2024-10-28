def count_vowels(file_path):
    try:
        vowel_count = 0
        vowels = 'aeiouAEIOU'
        with open(file_path, 'r') as file:
            content = file.read()
        
        for char in content:
            if char in vowels: 
                vowel_count += 1
        
        print(f"Number of vowels: {vowel_count}")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'P50.txt' 
count_vowels(file_path)