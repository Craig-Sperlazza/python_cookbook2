import csv 

####to read a file use DictReader
####gives you back an ordered dictionary

# with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/names.csv', 'r') as csv_file:
#     # csv_reader = csv.reader(csv_file)
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line)
#         print(line['email'])

#DictWriter method
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/new_dict_names.csv', 'w') as new_file:

        #must specify the keys 
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


#DictWriter method---WHY USE BEECAUSE IT IS EASIER TO MODIFY THE DATA----EXAMPLE DELETE THE EMAIL FIELD
with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/read_write_csv/mod_dict_names.csv', 'w') as new_file:

        #must specify the keys 
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)