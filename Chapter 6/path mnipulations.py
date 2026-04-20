import os
full_path=os.path.join('folder','subfolder','file.txt')
print("Full Path: ",full_path)
# split path
head, tail = os.path.split('/path/to/file.txt')
print("Head :", head)
print("Tail :",tail)
# get base name
basename = os.path.basename('/path/to/file.txt')
print("Basename:",basename)