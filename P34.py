def reverse_dictionary_keys(input_dict):
    reversed_dict = {key: input_dict[key] for key in reversed(input_dict.keys())}
    return reversed_dict

input_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

reversed_dict = reverse_dictionary_keys(input_dict)

print("Original Dictionary:", input_dict)
print("Reversed Dictionary:", reversed_dict)