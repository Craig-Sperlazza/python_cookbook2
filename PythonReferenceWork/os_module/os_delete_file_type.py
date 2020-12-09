#This program will look for specific file names or types in a given directory and delete them
#.jpg and "draft" is the default in this instance

# os.listdir(path)---returns a list containing the names of the entries in the directory given by the path
# os.path.isfile(path)----- return True if it is pointing at a file
# os.remove(file) -----deletes a given file
# any(iterable) function ----returns True if any element of an iterable is True. If not, any() returns False.
# string.startswith(sub_string) function returns True if a given string starts with substring

import os

to_delete = {
    'startswith': ['draft'],
    'endswith': ['.jpg', '.png']
}

my_path = '/home/craig/Desktop/os_test/'

files_list = [f for f in os.listdir(my_path) if os.path.isfile(my_path + '/' + f)]

print(files_list)

for filename in files_list:
    if any([filename.startswith(s) for s in to_delete['startswith']]):
        os.remove(my_path + '/' + filename)
        continue
    elif any([filename.endswith(s) for s in to_delete['endswith']]):
        os.remove(my_path + '/' + filename)
        continue