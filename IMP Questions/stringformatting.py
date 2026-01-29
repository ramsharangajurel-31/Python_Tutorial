# important questions

#  String Formatting

#  First Method
# Formatting with the % operator--------------------------------
# %s= string %d= integer
name = 'RamSharan'
age = 20
formatted_string = "Name : %s , Age : %d"%(name,age)
print(formatted_string)

print("===============================================================")
# second method
# Formatting with format() string Method ------------------------------
#  Syntax "string{}" . format(value)
name = "RamSharan"
age = 20
formatted_string = "Name:{}, Age:{}".format(name,age)
print(formatted_string)
formatted_string1 = "Name:{0}, Age:{1}".format(name,age)
print(formatted_string1)
formatted_string2 = "Name:{name}, Age:{age}".format(name=name,age=age )
print(formatted_string2)