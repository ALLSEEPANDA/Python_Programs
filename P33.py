def key_with_max_unique_values(input_dict):
    max_key = None
    max_unique_count = 0
    
    for key, values in input_dict.items():
        unique_values_count = len(set(values))
        
        if unique_values_count > max_unique_count:
            max_unique_count = unique_values_count
            max_key = key
    
    return max_key, max_unique_count

input_dict = {
    "a": [1, 2, 3, 4, 5],
    "b": [2, 3, 3, 3, 4, 4, 5],
    "c": [1, 2, 3],
    "d": [7, 8, 9, 10, 10]
}

max_key, max_unique_count = key_with_max_unique_values(input_dict)

print("Key with maximum unique values:", max_key)
print("Number of unique values:", max_unique_count)