# 15. Write a program to check whether a number is prime using for–else.
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not a Prime number")
        break
else:
    print("Prime number")
