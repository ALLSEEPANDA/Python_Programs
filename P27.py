def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

print("Average value of the numbers of the tuple of tuples:", average_tuple(nums))