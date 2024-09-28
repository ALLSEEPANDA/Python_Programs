l=[1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
i=0
while i < len(l) - 1:
    if l[i]==l[i+1]:
        l.pop(i)
    else:
        i+=1
print(l)