my_list = [1, 2, 3]
permutations = []

if len(my_list) == 1:
    permutations.append(my_list)

for i in range(len(my_list)):
    current_element = my_list[i]

    rest_of_list = my_list[:i] + my_list[i+1:]

    for p in [[x] for x in rest_of_list]:
        permutations.append([current_element] + p)

        for j in range(len(rest_of_list)):
            for q in [[x] for x in rest_of_list[:j] + rest_of_list[j+1:]]:
                permutations.append([current_element] + p + q)

for p in permutations:
    print(p)