import os

folder_path = input (r"Enter the folder path: ")

folder_name = os.path.basename(folder_path)

# size = os.path.getsize(r"C:\Users\anthd\Desktop\test2\writing.txt")
# print(size)

file_size = []

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path): # check if file, not folder
        size = os.path.getsize(file_path)
        file_size.append(size)

print(file_size)