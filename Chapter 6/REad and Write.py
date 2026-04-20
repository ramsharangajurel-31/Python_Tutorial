file = open('example.txt','r+')
content = file.read()
file.write('Adding new content')
file.close()