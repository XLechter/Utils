import numpy as np
import blobfile as bf

# get all the files in folder and subfolders in data_dir
def _list_image_files_recursively(data_dir):
    results = []
    for entry in sorted(bf.listdir(data_dir)):
        full_path = bf.join(data_dir, entry)
        ext = entry.split(".")[-1]
        if "." in entry and ext.lower() in ["jpg", "jpeg", "png", "gif", "npy"]:
            results.append(full_path)
        elif bf.isdir(full_path):
            results.extend(_list_image_files_recursively(full_path))
    return results
    
    
# select N items (files) from a list
original_list = _list_image_files_recursively(data_dir)
N = 5000
selected_list = random.choices(original_list, k=N)
print(len(selected_list))


# get parent folder with os
import os
file_path = '/home/user/Downloads/test'
parent_directory = os.path.dirname(file_path)
print(parent_directory)

