def count_uppercase_and_digits(file_path):
    try:
        uppercase_count = 0
        digit_count = 0
        
        with open(file_path, 'r') as file:
            content = file.read()
        
        for char in content:
            if char.isupper():  
                uppercase_count += 1
            if char.isdigit():  
                digit_count += 1
        
        print(f"Number of uppercase characters: {uppercase_count}")
        print(f"Number of digits: {digit_count}")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'P49.txt'  