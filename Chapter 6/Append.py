#
file=open('example.txt','a+')
file.write("Appending a new line")
file.seek(0)
content = file.read()
file.close()