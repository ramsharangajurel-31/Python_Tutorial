def greet(name):
    print("Hello, " + name + "!")

print(greet("Bob"))
print(greet("Alice"))


# modularity
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
sum_result = add(10,20)
print(sum_result)
product_result = multiply(10,20)
print(product_result)

#
def sum(a,b):
    c= a+b
    print(c)
sum(2,3)


# reusability
def calculate_area(radius):
    pi = 3.14159
    return pi*radius*2

print(calculate_area(10))


# maintainability
def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
def convert_to_fahrenheit(celsius):
    return (celsius*9/5)+32
temp_c=convert_to_celsius(100)
print(temp_c)
temp_f=convert_to_fahrenheit(37.78)
print(temp_f)

# testing and debugging
def is_even(num):
    return num%2==0
assert is_even(5)==False
assert is_even(4)==True

# abstraction
def fetch_data_from_api(api_endpoint):
    pass
data = fetch_data_from_api("https://api.example.com/data")


# function with return values
def square (number):
    return number**2
result = square(10)
print(result)

# default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Bob")
greet()
# -----------------------------------------------imp------------------------------------------------
# keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I am {animal_type}, {pet_name}")
describe_pet(animal_type="dog", pet_name="Rex")
describe_pet(pet_name="cat", animal_type="dog")


# variable lenght arguments
def make_pizza(size, *toppings):
    print(f"Making a {size} inch  pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(12,"pepperoni", "mushrooms", "green peppers", "extra cheese")

# lambda functions
add =lambda a,b: a+b
print(add(10,20))

square = lambda num: num**2
print(square(10))

# positional arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")
describe_pet("dog", "rex")

# keyword arguments
describe_pet(animal_type="cat", pet_name="Whiskers ")
describe_pet(animal_type="Fish", pet_name="Goldie ")

# default arguments
def describe_pet(animal_type ='Cat', pet_name='Mouse'):
    print(f"I have a {animal_type} named {pet_name}")
describe_pet()
# default arguments
def describe_pet(pet_name, animal_type='Cat'):
    print(f"I have a {animal_type} named {pet_name}")
describe_pet(pet_name="Mouse")
describe_pet("Whiskers","Cat")