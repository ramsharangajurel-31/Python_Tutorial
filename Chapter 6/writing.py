with open('example.txt', 'w') as file:
    file.write("Hello World!\n")

# writing multiple lines(writelines())
lines = ['Line1\n', 'Line2\n', 'Line3\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)






























