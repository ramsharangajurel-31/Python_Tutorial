# pattern numbers
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
print ("---------------------------------------")
# reverse a triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print ("---------------------------------------")

#hollow square pattern
n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("---------------------------------------")

# pyramid pattern
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

print("---------------------------------------")

# reversed right angle triangle
n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("---------------------------------------")

# star triangle

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


print("---------------------------------------")


# number triangle

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



print("---------------------------------------")



# alphabelt triangle
n = 5
for i in range(1, n + 1):
    for j in range(65, 65 + i):  # ASCII code for A=65
        print(chr(j), end=" ")
    print()
