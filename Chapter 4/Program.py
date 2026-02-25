# function thst takes the arguments and return the greatest number
def greatestNumber(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print(greatestNumber(10,25,15))



# function to find the sum of any numbers passed to it
def find_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(find_sum(1,2,3,4,5))
print(find_sum(3,4,5))
