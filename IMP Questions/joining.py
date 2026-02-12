# joining
# using the + operator
t1 = (1,2,3)
t2 = (4,5,6)
joined = t1 + t2
print(joined)

# using sum with a list of tuples
tuples_list =[(1,2),(3,4),(5,6)]
joined_tuple = sum(tuples_list,())
print(joined_tuple)
# nested tuple joining
t1=[1,2,3]
t2=[4,5,6]
nested_tuple = (t1,t2)
print(nested_tuple)

# using a loop to join tuples
tuples_list =[(1,2),(3,4),(5,6)]
joined_tuple =()
for t in tuples_list:
    joined_tuple +=t
print(joined_tuple)
#  efficient way to join tuples
tuples_list =[(1,2),(3,4),(5,6)]
temp_list = []
for t in tuples_list:
    temp_list.extend(t)
joined_tuple = tuple(temp_list)
print(joined_tuple)