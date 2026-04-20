# write a program in python to write a single sentence , then add two more sentence and show all the sentences on the screen using the file handling
# write a single sentence
file=open("sentences.txt","w")
file.write("Python is powerful programming language.\n")
file.close()
# add two more sentences
file=open("sentences.txt","a")
file.write("Python is widely used in data science.\n")
file.write("Python supports data science.\n")
file.close()
# read and display all sentences
file=open("sentences.txt","r")
content=file.read()
file.close()
print("Content of the file:---------")
print(content)
# write a program to copy the content of the one file to a another file named copy.txt==============================
# open the source file in read mode
source=open("sentences.txt","r")
# read the content from the source file
content=source.read()
file.close()
# open the destiantion file in write mode
destination=open("copy.txt","w")
# write contents to copy.txt
destination.write(content)
destination.close()
print("File copied successfully in copy.txt")
