def generate_square_dict(n):
    square_dict = {x: x * x for x in range(1, n + 1)}
    return square_dict

n = 10  
square_dict = generate_square_dict(n)

print("Generated Dictionary:", square_dict)