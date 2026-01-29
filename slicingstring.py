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

print("=================================================")


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

print ("==================================================")

 # slicing
str4= "Hello World"
first_word=str4[:5]
print(first_word)

print("======================================================")
 #  reversed
s="Hello World"
reversed_s=s[::-1]
print(reversed_s)

print("======================================")

 # every third character
str5="Hello World"
every_third_char=str5[-3:]
print(every_third_char)

print("=========================================")

# last word
str6="Hello World"
last_word=str6[:7]
print(last_word)

# every second character
str7="Hello World"
every_second_char=str7[::2]
print(every_second_char)

print("==========================================")
# others
s="Hello World"
# extract hello world using negative indices
world=s[-6:-1]
print(world)

# extract "Hello"using a combination of positive slicing and step
hello = s[0:5:1]
print(hello)

# reverse
reversed_hello=s[4::-1]
print(reversed_hello)




