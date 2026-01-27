# 16. Write a program to search an element in a list using for–else.
lst = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

for item in lst:
    if item == key:
        print("Element found")
        break
else:
    print("Element not found")
