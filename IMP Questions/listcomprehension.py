
# List Comprehension भनेको Python मा छोटो, सफा र सजिलो तरिकाले नयाँ list बनाउने विधि हो। यसले loop र condition लाई एकै लाइनमा लेख्न मद्दत गर्छ।
# syntax [expression for item in iterable


#  creating a list of squares
squares =[x**2 for x in range(10)]
print(squares)
# iterating with a condition
events = [x for x in range (10) if x%2==0]
print(events)
#  applying A FUNCTION TO EACH ELEMENT
fruits = ['apple','banana','orange']
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

#  nested list comprehension
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)