def find_divisible_tuples(tuples_list, K):
    result = []
    for tup in tuples_list:
        all_divisible = True  
        for elem in tup:
            if elem % K != 0:  
                all_divisible = False  
                break  
        if all_divisible:
            result.append(tup)
    return result

tuples_list = [(2, 4, 6), (3, 6, 9), (10, 20), (15, 30), (1, 2, 3)]
K = 2
divisible_tuples = find_divisible_tuples(tuples_list, K)
print(divisible_tuples)