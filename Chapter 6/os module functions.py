import os
#
# current_directory = os.getcwd()
# print("Current directory:", current_directory)
#
# # change directory (use a valid path)
# new_path = r"C:\Users\Ram Sharan Gajurel\Documents"
# os.chdir(new_path)
#
# print("Changed to:", os.getcwd())
#
# # list directory contents
# files = os.listdir('.')
# print("Files:", files)
#
# # create directory
# os.mkdir('new_directory')
#
# # remove directory
# os.rmdir('new_directory')

# working with files===================================================================
# if os.path.exists('example.txt'):
#     print("File exists")
# else:
# #     print("File doesn't exist")
# # # rename a file or directory
# os.rename('new_name.txt', 'example.txt')
# get file size
size=os.path.getsize('example.txt')
print (size)