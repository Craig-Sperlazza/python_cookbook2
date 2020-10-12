# https://www.youtube.com/watch?v=tJxcKyFMTGo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=10

import os
from datetime import datetime

# if you want to see all the methods available
# print(dir(os))

# print cwd -> /home/craig/Desktop/python_cookbook2
print(os.getcwd())

# navigate to desktop from current directoy (back one)
os.chdir('/home/craig/Desktop')
print(os.getcwd())

############################################################################################################################
# lets see what directories are on the Desktop (can pass a path but the default is current)
#print(os.listdir())

#########################################################################################################################
# lets make osdemo2 folder on the Desktop---2 methods (make dirs will make all intermediate folders too)---use makedirs
# os.mkdir('osdemo2')
# os.makedirs('osdemo2')

# os.makedirs('osdemo2/subfolder')

# lets remove the dir rmdir() and removedirs() ---usually use rmdir so we dont accidentally delete too much
# os.rmdir('subfolder')
# os.rmdir('osdemo2')
# os.removedirs('osdemo2/subfolder')

############################################################################
#rename a file or folder
# os.mkdir('original')
# os.rename('original', 'new_name')
############################################################################

# #How to Find file attributes
# #make a fake file on desktop name test.txt
# all_fields = os.stat('test.txt')
# print(all_fields)

# #how to get last modified in human readable
# mod_time = os.stat('test.txt').st_mtime
# human_read = datetime.fromtimestamp(mod_time)
# print(human_read)

##############################################################################
# os.walk traverses down from the directory you pass and foes into each subdirectory, and so on
#use case---know the name of file but arent sure exactly where it is 

# cur_dir = os.getcwd #'/home/craig/Desktop' could pass in the string directly
# for dirpath, dirnames, filenames in os.walk('/home/craig/Desktop/python'):
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)

################################################################################
# os.path.join allows us to join two file paths together and it ensures correct syntax
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

####################################################################################
#miscellaneous useful methods in os.path
print(os.path.basename('testdir/tmp/test.txt')) #returns the filename: test.txt
print(os.path.dirname('testdir/tmp/test.txt')) #returns the directories: tesrdir/tmp
print(os.path.split('testdir/tmp/test.txt')) #returns: ('testdir/tmp', 'test.txt')
print(os.path.exists('testdir/tmp/test.txt')) #returns True if path exists

#if you know the path exists but dont know if it is a directory or file
print(os.path.isdir('/tmp/adfads')) #returns True if adfads is a directory
print(os.path.isfile('/tmp/adfads')) #returns True if adfads is a file

#easy way to split off the extension
print(os.path.splitext('/tmp/test_file.txt')) # returns: ('/tmp/test_file', '.txt')

#################################################################################################
# Execute programs
os.system("dir")
os.system("ls")

dirList = os.listdir()
for filename in dirList:
    print filename