l = [0, 1, 0, 2, 0, 3, 0, 4]
nonZeros = []
zeros = []
for i in l:
    if i==0:
        zeros.append(i)
    else:
        nonZeros.append(i)
l=nonZeros+zeros
print(l)