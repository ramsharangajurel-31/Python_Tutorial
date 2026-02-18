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



