# https://www.youtube.com/watch?v=tJxcKyFMTGo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=10

import os

# if you want to see all the fmethods available
# print(dir(os))

# print cwd
print(os.getcwd())

# navigate to desktop from current directoy (back one)
os.chdir('/home/craig/Desktop')
print(os.getcwd())

# lets see what directories are on the Desktop (can pass a path but the default is current)
print(os.listdir())

# lets make osdemo2 folder on the Desktop---2 methods (make dirs will make all intermediate folders too)---use makedirs
# os.mkdir('osdemo2')
# os.makedirs('osdemo2')

os.makedirs('osdemo2')

# lets remove the dir rmdir() and removedirs() ---usually use rmdir so we dont accidentally delete too much

os.rmdir('osdemo2')
