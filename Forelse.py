# break using for else

numbers = [1,2,3,4,5,6]
for number in numbers:
    if number ==  6: break
    print(number)
else:
    print("Continue withot breaking")
# break
for num in range(10):
    if num == 5:
        break # Exit the loop when num is 5
    print(num)

# continue
for num in range(10):
    if num == 5:
        continue # Exit the loop when num is 5
    print(num)

#     pass statement
num = int(input("Enter a number: "))

if num == 5:
    pass
elif num == 6:
    print("Number is 6")
else:
    print("Number is not 6")

# program to check if the number is negative positive or zero
num = int(input("Enter a number: "))
if num > 0:
    print ("This is a Positive Number")
elif num <0:
    print ("This is a Negative Number")
else:
    print ("This is a Zero")

# program to find the sum of natural numbers up tp a given number using a while loop
total = 0
number = int(input("Enter a number: "))
i = 1

while i <= number:
    total = total + i
    i = i + 1

print(total)


# program to print a prime number given by a user
num = int(input("Enter a number: "))

if num <= 1:
    print("  This is not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("This is not a Prime Number")
            break
    else:
        print(" This is Prime Number")

# program to print all prime numbers within a range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
