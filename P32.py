def replace_with_kth_value(input_string, replacement_dict, k):
    words = input_string.split()
    result = []
    
    for word in words:
        if word in replacement_dict and len(replacement_dict[word]) >= k:
            result.append(replacement_dict[word][k - 1])
        else:
            result.append(word)
    
    return ' '.join(result)

input_string = str(input("Enter String: "))
replacement_dict = {
    "apple": ["fruit", "healthy", "red"],
    "banana": ["yellow", "fruit", "long"],
    "orange": ["fruit", "citrus", "round"]
}
k = int(input("Enter the Kth value: "))

output = replace_with_kth_value(input_string, replacement_dict, k)
print("Output:", output)