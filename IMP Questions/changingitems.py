# changing items -------------------------------
import copy

my_list=[10,20,30,40,50]
# changing the second item
my_list[1]
print(my_list)

# changing the second and the third items
my_list[1:3]=[25,35]
print(my_list)

# changing the range of the items with a different number of elements
my_list[1:4]=[22,32]
print(my_list)

# adding items------------------------------------------------------------------
my_list=[10,20,30,40,50]
# adding a single item to the end of the list
my_list.append(60)
print(my_list)

# adding a single item at a specific index
my_list.insert(2,25)
print(my_list)

# ading the multiple items to the end of the list
my_list.extend([70,80])
print(my_list)

# removing items---------------------------------------------------------------------
my_list=[10,20,30,40,50]
# removing a specific items by value
my_list.remove(30)
print(my_list)
# removing an item by index and returning it
removed_item=my_list.pop(1)
print(removed_item)
print(my_list)

# removing an item by index without returning it
del my_list[0]
print(my_list)

# removing a range of items using slicing
my_list=[10,20,30,40,50]
del my_list[1:3]
print(my_list)

# clearing a list---------------------------------
my_list=[10,20,30,40,50]
# clearing a list
my_list.clear()
print(my_list)

# looping --------------------------------------
# using a for loop
my_list=[10,20,30,40,50]
for item in my_list:
    print(item)

    # using a for loop with enumerate()
my_list=[10,20,30,40,50]
for index,item in enumerate(my_list):
    print(f"Index:{index}, Item:{item}")

# using a while loop
my_list=[10,20,30,40,50]
i=0
while i<len(my_list):
    print(my_list[i])
    i=i+1

# copying (shallow copy/deep copy)-------------------------------------------
# using copy() method
original_list=[10,20,30,40,50]
copy_list=original_list.copy()
print(copy_list)

# copying using slicing
original_list=[10,20,30,40,50]
copy_list=original_list[:]
print(copy_list)
# using list() constructor
original_list=[10,20,30,40,50]
copied_list=list(original_list)
print(copied_list)


# using copy modules copy() function
original_list=[1,2,3,4,5]
copied_list=copy.copy(original_list)
print(copied_list)

# using copy modules deepcopy() function
original_list=[1,2,3,4,5]
copied_list=copy.deepcopy(original_list)
print(copied_list)


# modify the copied list won't afect the original list
copied_list[2][0]=99
print(copied_list)
print(original_list)