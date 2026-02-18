# using curly braces
my_dict = {
    "name" : "Ram",
    "age" : 25,
    "city" : "New York"
}
print(my_dict)
print(type(my_dict))

# uing the dict() function
my_dict = dict(name="Ram", age=25, city="New York")
print(my_dict)


# Creating a dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "London"
}
# Adding a new key-value pair
person["email"] = "john@example.com"
print(person)

# Updating an existing value
person["age"] = 26
print(person)

# Using update() to add and update multiple key-value pairs
person.update({"phone": "555-1234", "city": "Manchester"})
print(person)



# creating a dictionary
person = {
    "name": "Ram",
    "age": 25,
    "city": "New York",
    "email" : "ram@example.com",
    "phone" : "555-1234"
}

# using del to remove an item
del person["email"]
print(person)
#  using () pop to remove an item and gets its value
age=person.pop("age")
print(age)
print(person)

# using popitem() to remove the last item
last_item = person.popitem()
print(last_item)
print(person)

# using clear to remove all items
person.clear()
print(person)


# binary types
x=b"HelloWorld"
print(x)
data=b'\x48\x65\x6c\x6C\x6C\x6f'
print(data)
lst = [1,2,3]
y=bytes(lst)
print(y)


# bytearray
mutable_data = bytearray(b'\x48\x65\x6c\x6C\x6C\x6F')
mutable_data[0] = 0X41
print(mutable_data)

# memoryview
x = bytearray(b"hello world")
m = memoryview(x)
print(m)


# nonetype
def do_nothing():
    pass
result=do_nothing()
print(result)
