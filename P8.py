num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the Third number: "))

if num1 >= num2 and num1 >= num3:
    big_num = num1
elif num2 >= num1 and num2 >= num3:
    big_num = num2
else:
    big_num = num3

print("The biggest number is: ", big_num)