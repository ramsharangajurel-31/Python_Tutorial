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
# num = int(input("Enter a number: "))
#
# if num == 5:
#     pass
# elif num == 6:
#     print("Number is 6")
# else:
#     print("Number is not 6")

# program to check if the number is negative positive or zero
num = int(input("Enter a number: "))
if num > 0:
    print ("This is a Positive Number")
elif num <0:
    print ("This is a Negative Number")
else:
    print ("This is a Zero")

# program to find the sum of natural numbers up tp a given number using a while loop
num = int(input("Enter a number: "))



# program to print all the prime numbers within a range