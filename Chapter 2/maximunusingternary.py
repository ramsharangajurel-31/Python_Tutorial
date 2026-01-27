# 6. Write a program to find maximum of two numbers using ternary operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = a if a > b else b
print("Maximum number is", max_num)
