# slicing with start and end
str1 = "RamSharan"
print(str1[0:5])
print(str1[:5])
print(str1[:])
"'whole string '"

print(str1[3:])
print(str1[2:5])

# syntax of slicing
# string[ start:end:step]
# default step :1
# ending index = exclusive
# starting index = inclusive

print("----------------------------------------------")


# slicing with negative indices
str2 = "RamSharan"
print(str2[-6:-1])
print(str2[:])


print("================================================")
# slicing with step
str3 = "RamSharan"
print(str3[::2])
print(str3[1::2])
print(str3[::-1])