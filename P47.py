def count_letter_a(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()  

        count_a = content.lower().count('a')  

        print(f"The letter 'a' appears {count_a} times in the file.")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'P47.txt'  
count_letter_a(file_path)