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

# removing items=========================================================================================
# remove(element): Removes a specified element; raises KeyError if not found.
# discard(element): Removes a specified element; does nothing if not found.
# pop(): Removes and returns an arbitrary element; raises KeyError if the set is empty.
# clear(): Removes all elements from the set.

# creating and adding items
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
print("After adding items:", my_set)


# removing items
my_set.remove(2)
my_set.discard(3)
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("After removing items:", my_set)

# clearing the set
my_set.clear()
print("after clearing the set:", my_set)

# set operations ===================================important==================================================
set1 = {1,2,3,4,5}
set2= {4,5,6,7,8}
# union of set 1 and set 2
union_set=set1.union(set2)
print(f"union set: {union_set}")

# intersection of set 1 and set 2
intersection_set=set1.intersection(set2)
print(f"intersection set: {intersection_set}")

# difference of set 1 and set 2
difference_set=set1.difference(set2)
print(f"difference: {difference_set}")

# symmetric difference of set 1 and set 2
symmetric_set=set1.symmetric_difference(set2)
print(f"symmetric set: {symmetric_set}")

# check if set 1 is a subset of set 2
is_subset=set1.issubset(set2)
print(f"is_subset: {is_subset}")

# check if set 1 is a superset of set 2
is_superset=set1.issuperset(set2)
print(f"is_superset: {is_superset}")

# check if set 1 and set 2 are disjoint
is_disjoint=set1.isdisjoint(set2)
print(f"is_disjoint: {is_disjoint}")