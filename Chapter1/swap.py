# 8. Write a program to swap two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)