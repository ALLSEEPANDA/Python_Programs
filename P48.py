def replace_a_with_z(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
                   
        modified_content = content.replace('A', 'Z')
        print(modified_content)
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'P48.txt' 
replace_a_with_z(file_path)