with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    # reading a specific number of characters
with open('example.txt', 'r') as file:
    content = file.read(10)
    print(content)
# reading a single line
with open('example.txt', 'r') as file:
    line = file.readlines()
    print(line)
# reading all lines
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
# iterating over file object
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
