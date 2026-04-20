import os

file_path = "path_to_file_to_delete"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("The file does not exist or the path is incorrect.")