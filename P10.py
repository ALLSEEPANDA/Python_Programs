names = "Mohan Sharma; Ajay Gahlot; Amit Mathur; Vijay Kumar; Kunal Kumar"

individual_names = names.split("; ")
print(individual_names)
first_names = []
second_names = []

for name in individual_names:
    split_name = name.split()
    first_names.append(split_name[0])
    second_names.append(split_name[1])

print("First Names:")
for name in first_names:
    print(name)

print("\nSecond Names:")
for name in second_names:
    print(name)