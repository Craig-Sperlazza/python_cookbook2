#linux version
#Corey Schaffer
#https://www.youtube.com/watch?v=PUIE7CPANfo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=13

#in terminal: 
# python3 ----to see what version, if it works it means it found it on our path
# which python3 or type python3 ------gives us the path to your python---note you could use the full path to run your program
#for example, if you know where anaconda is, you can use that full path to run the program instead of python3
# 
#echo $PATH ----gives us where the program will look for python3 in order
#
#.bashrc file in the home directoy----it has our conda setup, or it should. If not, you can specifiy a PATH yourself anaconda or other
# see around(9:00 mark of video) to allow yourself to set your path priority

#how to see what version of python you are actaully executing, may have to rearrange path if you are 
import sys
import django
print(sys.version)
print(sys.executable)

#python and pip-----install a package but then cant use it----likely that your path is messed up and pip is 
# installing it and python is looking in different places
#you can fix this correctly by fixing the .bashrc file
#but it appears to fix correctly in vscode if you switch the version (bottom left)

