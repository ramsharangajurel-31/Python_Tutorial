# 11. Write a program to find factorial of a number using for loop.
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial is", fact)
