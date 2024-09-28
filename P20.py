l=['Python', 'list', 'exercises', 'practice', 'solution']
Sl=[]
for i in l:
    Slstr=''.join(sorted(i))
    Sl.append(Slstr)
print(Sl)