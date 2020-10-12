
#recommended to use a context manager IT IS BEST PRACTICE

#r read
#a appends to end of file
#w overwrites existing file content

#always close() files you use

# f = open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

#########################################################################################################################
# context mangers----allow us to work within the file block but then automatically closes it when the block executes or if there is an error
#can read the whole file or parts thereof

# with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test.txt', 'r') as f:
#     # f_contents = f.read(100) #f.read()loads the entire file unless you pass in a size (100 characters for example)
#     # print(f_contents)
#     # 
#     # f_contents = f.read(100) # if you pass it again, it prints the next 100 characters
#     # print(f_contents)
#     #
#     #f.seek(0) would change positioon back to beginning but you can pick any position you want
#     #
#     #When you get to end, it will print empty string

#     #BEST METHOD
#     size_to_read = 10

#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:
#         # print(f_contents, end='*')#* makes it more obvious how python is doing this
#         print(f_contents, end='')#
#         f_contents = f.read(size_to_read)

# #CAN READ LINES 
# with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test.txt', 'r') as f:
#     # f_read_lines = f.readlines() #every line of file is an element in a list
#     # print(f_read_lines)
#     #
#     #
#     # f_read_line = f.readline() #goes line by line of file ---first line----end gets rid of extra lines that python adds
#     # print(f_read_line, end='') 
#     # f_read_line = f.readline() #goes line by line of file ---secondline line
#     # print(f_read_line, end='') 

#     #most efficient way to print lines---does NOT read in entire contents at once
#     for line in f:
#         print(line, end='')

# #################        WRITE TO FILES NOTE a vs w     ###############################################
# with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test2.txt', 'a') as f:
#     f.write('Test Input Text')

####################Read and Write Together Example#########################
#open a file, write to a file that does not exist yet and write the read file line by line to the write file
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test.txt', 'r') as rf:
    with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

################copy a large IMAGE file##########################################
# must open the file in binary mode-----rb, wb
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/robot.jpg', 'rb') as rfb:
    with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_files/picture_copy.jpg', 'wb') as wfb:
        for line in rfb:
            wfb.write(line)


#CONVERT A LINE FROM A FILE TO AN ARRAY
#example for piazza
# Hi Ashley,

# If you are trying to convert one line from the input file to the array of, say, integers, here's what you can do in Python:

# # assume the line from the data.txt file was read to variable line: str

# line = line.strip()	      					# remove the newline character
# arr_str = line.split(' ')						# convert into array using ' ' as element separator
# arr_int = list(map(int, arr_str)    # convert each array element from str to int type
# arr = arr_int[1:]                   # get rid of leading elemetns since it is same as len(arr)
# Of course, like most things in Python, this can be converted to a one-liner:

# arr = list(map(int, line.strip().split(' ')))[1:]