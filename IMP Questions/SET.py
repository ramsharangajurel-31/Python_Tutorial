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