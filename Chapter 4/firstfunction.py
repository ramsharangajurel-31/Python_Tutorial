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


# reusability
def calculate_area(radius):
    pi = 3.14159
    return pi*radius*2

print(calculate_area(10))