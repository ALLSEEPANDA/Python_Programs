dec = int(input("Enter a Decimal No. Between 10 to 100 : "))

binary = ''
while dec > 0:
    binary = str(dec % 2) + binary
    dec //= 2

print(binary)