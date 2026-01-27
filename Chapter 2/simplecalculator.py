# 5. Write a program to create a simple calculator using if–elif–else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")
