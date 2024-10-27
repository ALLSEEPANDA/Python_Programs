def element_wise_sum(*tuples):
    return tuple(sum(x) for x in zip(*tuples))

tup1 = (1, 2, 3, 4)
tup2 = (3, 5, 2, 1)
tup3 = (2, 2, 3, 1)

result = element_wise_sum(tup1, tup2, tup3)
print("Element-wise sum of the said tuples:", result)
