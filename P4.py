'''Defined Variables for Arithmetic,
Relational,Logical,Bitwise and Ternary'''
x = 10
y = 5

# Arithmetic Operations
print("Arithmetic Operations:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Floor Division:", x // y)

# Relational Operations
print("\nRelational Operations:")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)

# Assignment Operations
z = 15
print("\nAssignment Operations:")
print("Initial Value of z:", z)
z = 15
z += 5
print("z after += 5:", z)
z = 15
z -= 5
print("z after -= 5:", z)
z = 15
z *= 5
print("z after *= 5:", z)
z = 15
z /= 5
print("z after /= 5:", z)
z = 15
z %= 5
print("z after %= 5:", z)
z = 15
z //= 5
print("z after //= 5:", z)
z = 15
z **= 5
print("z after **= 5:", z)
z = 10
z &= 5
print("z after &= 5:", z)
z = 10
z |= 5
print("z after |= 5:", z)
z = 10
z ^= 5
print("z after ^= 5:", z)
z = 10
z >>= 5
print("z after >>= 5:", z)
z = 10
z <<= 5
print("z after <<= 5:", z)

# Logical Operations
print("\nLogical Operations:")
print("And Operation:", x > 3 and x < 10)
print("Or Operation:", x > 3 or x < 4)
print("Not Operation:", not(x > 3 and x < 10))

# Bitwise Operations
print("\nBitwise Operations:")
print("Bitwise And:", x & y)
print("Bitwise Or:", x | y)
print("Bitwise Xor:", x ^ y)
print("Bitwise Not:", ~x)
print("Left Shift:", x << 2)
print("Right Shift:", x >> 2)

# Ternary Operation
print("\nTernary Operation:")
print("Hello" if x < y else "Bye")

# Membership Operations
a = ["apple", "banana"]
print("\nMembership Operations:")
print("Is 'banana' in the list?", "banana" in a)
print("Is 'pineapple' not in the list?", "pineapple" not in a)

# Identity Operations
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("\nIdentity Operations:")
print("Is x identical to z?", x is z)
print("Is x identical to y?", x is y)
print("Is x not identical to z?", x is not z)
print("Is x not identical to y?", x is not y)