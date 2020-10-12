#CONVERT A LINE FROM A FILE TO AN ARRAY

# If you are trying to convert one line from the input file to the array of, say, integers, here's what you can do in Python:

with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_string_to_array/numbers.txt', 'r') as rf:
    rf_contents = rf.read()
    # print(rf_contents)
    line = str(rf_contents)
    # assume the line from the data.txt file was read to variable line: str

    # print(line)
    strip_line = line.strip()	      					    # remove the newline character
    # print(strip_line)
    arr_str = strip_line.split('\n')						# convert into array using ' ' as element separator---I had to use /n, not sure why
    
    arr_int = list(map(int, arr_str))                # convert each array element from str to int type
    new_arr = arr_int[0:]                              # get rid of leading elemetns since it is same as len(arr)
    print(new_arr)
    
    #in his example he had to get rid of something at the beginning of the array, we didnt here.
    # arr_int = list(map(int, arr_str))                # convert each array element from str to int type
    # new_arr = arr_int[1:]                              # get rid of leading elemetns since it is same as len(arr)
    

    # Of course, like most things in Python, this can be converted to a one-liner:

    #arr = list(map(int, line.strip().split(' ')))[1:]