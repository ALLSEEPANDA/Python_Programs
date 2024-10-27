from collections import Counter

def sort_counter_by_value(data):
    counter = Counter(data)
    sorted_data = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return sorted_data

data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

sorted_result = sort_counter_by_value(data)
print("Sorted Counter by Value:", sorted_result)