import os

folder_path = input (r"Enter the folder path: ")

folder_name = os.path.basename(folder_path)

file_size = {}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path): # check if file, not folder
        size = os.path.getsize(file_path)
        file_size[file] = size

largest_file = max(file_size.values())

for key, value in file_size.items():
    if value == largest_file:
        # file extension needs to be preserved (folders don't have file types)
        old_path = os.path.join(folder_path, key)
        name, ext = os.path.splitext(key)
        new_path = os.path.join(folder_path, folder_name + ext)
        os.rename(old_path, new_path)
        print(key, 'renamed to', folder_name + ext)
    else:
        extras_path = os.path.join(folder_path, 'Extras')
        os.makedirs(extras_path, exist_ok=True) # create Extras folder
        file_path = os.path.join(folder_path, key)
        os.rename(file_path, os.path.join(extras_path, key))
        print('moved', key, 'to', extras_path)
        
        
