# https://www.geeksforgeeks.org/python-os-mkdir-method/

import os

print(os.getcwd())

# this will work with all modules to give us the location of the file----this shows us the entire standard library
# print(os.__file__)

#
# NOTE: if you only create a directory it creates it in the python_cookbook2 (i.e. what you get from os.getwd())
# So if you want to go up a level to the desktop in this case, use ../ as path
#
#

# Directory
directory = "GeeksForGeeks"


# Parent Directory path
parent_dir = "../"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '%s' created" % directory)

os.mkdir(directory)
print("Directory '%s' created" % directory)
