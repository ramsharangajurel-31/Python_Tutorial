# sorting---------------------------------------------------------------------------------------------
# basic sorting
from typing import Any

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.sort()
print(my_list)

# sorting in  descending order
my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.sort(reverse=True)
print(my_list)

# sorting with a  custom key
my_list = [ 'apple', 'banana', 'cherry', 'date' ]
my_list.sort(key=len)
print(my_list)

# sorted=====================================================================================================
# -returns a new sorted list and leaves the original list unchanged

# basic sorting
my_list =[1,2,3,4,5,6,7,8,9,10]
sorted_list = sorted(my_list)
print(sorted_list)
print(my_list)

# sorting in descending order
my_list = [40,30,20,10]
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)

# sort with a custom key
my_list = ['apple', 'banana', 'cherry', 'date']
sorted_list = sorted(my_list, key=len)
print(sorted_list)

#  joining ==============================================================================================
#  it involves combining multiple lists .. joining list elements into a single string

#  using a + operator
list1=[1,2,3]
list2=[4,5,6]
combined_list=list1+list2
print(combined_list)
#  using the extended method
list1 =[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

#  using the * operator for repeated concatenation
list1=[1,2,3]
repeated_list=list1*3
print(repeated_list)

# joining list element into a string
words = ['Hello', 'World' , 'From', 'Python']
sentence = ' '.join(words)
print(sentence)


# joing characters
characters =['a,b,c']
joined_string=' '.join(characters)
print(joined_string)

# using a list comprehension
nested_list=[ [1,2],[3,4], [5,6] ]
flat_list= [item for sublist in nested_list for item in sublist]
print(flat_list)


#  tuple> a collection of ordered , immutable elements-------------------------------------------------
#  creating a tuple
tuple1 =('1','2,' '3', 'a','b' , 'c')
print(tuple1)
#  creating a tuple without parenthesis
tuple2 = 1,2,3,4,5,6
print(tuple2)
# creating a empty tuple
empty_tuple = ()
print(empty_tuple)
#  creating a tuple witj one element
single_element_tuple = (1,)
print(single_element_tuple)
print(type(single_element_tuple))

# indexing and slicing in tuple
tuple1 =[1,2,3,4,5,6,7,8,9,10]
# positive indexing
print (tuple1[0])
print (tuple1[3])

# negative indexing
print (tuple1[-1])
print (tuple1[-2])


# slicing
tuple1 =(1,2,3,4,5,6,7,8,9,100)
# basic slicing
print(tuple1[1:3])

# ommiting start
print(tuple1[:3])

# omitting end
print(tuple1[2:])

# ommiting both start and end
print(tuple1[:])

# slicing with step
print(tuple1[1:5:2])
print(tuple1[::2])
