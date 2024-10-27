def count_frequencies(input_list):
    frequency_dict = {}
    
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    
    return frequency_dict

if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 4, 5]
    frequencies = count_frequencies(my_list)
    print(frequencies)