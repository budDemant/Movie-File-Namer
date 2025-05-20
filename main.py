import os

file_path = input (r"Enter the file path: ")

parent_folder_name = os.path.basename(os.path.dirname(file_path))
print(parent_folder_name)