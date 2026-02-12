my_set={(1,2),3,'hello'}
print(my_set)
my_set.add((4,5))
print(my_set)
# my_set.add([1,2,3])
# print(my_set)
my_set.remove(3)
print(my_set)
# creating a set
my_set={1,2,3,4,5}
print(my_set)
# using the set function
my_set = set([1,2,3,4,5])
print(my_set)
# creating a empty set
empty_set = set()
print(empty_set)

# iteration in set------------------------------------------------------------------------------------------------
my_set = {1,2,3,4,5}
for item in my_set:
    print(item)

    # checking membership--------------------------------1 marks --------------------------------------
my_set = {1,2,3,4,5}
# check if an element is in the set
print (3 in my_set)
print ( 6 in my_set)

# bikashey chor
# converting to a set
my_set = {1,2,3,4,5}
my_list = list(my_set)
print(my_list[0])

# using a built in functions
my_set = {1,2,3,4,5}
# get the number of elements
print(len(my_set))
# get the smallest element
print(min(my_set))
# get the largest element
print(max(my_set))

# get the sum of elements
print(sum(my_set))

# adding item to a set -------------------------------------------------------------------
# add() - to add single element
# update- to add multiple element
my_set = {1,2,3,4,5}
# adding a single it    em
my_set.add(6)
print(my_set)

# add aN item that already exist
my_set.add(2)
print(my_set)
# Create a set
my_set = {1, 2, 3}

# Add multiple items
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Add items from another set
another_set = {7, 8}
my_set.update(another_set)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Add items from a string (each character is added)
my_set.update("abc")
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c'}

