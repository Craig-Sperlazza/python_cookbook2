# https://www.youtube.com/watch?v=q5uM4VKywbA&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=15

# https://www.w3resource.com/python-exercises/csv/index.php

import csv 

####to read a file
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # #if the delimiter is not the default ',', you must specify what the delimter is, such as tab or -
    # csv_reader = csv.reader(csv_file, delimiter = '\t') 


    #if you dont want the header
    #next(csv_reader)

    #print data in csv_reader
    for line in csv_reader:
        print(line)
        #print(line[2])

#to write to a new csv file and use dashes instead of commas
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)


