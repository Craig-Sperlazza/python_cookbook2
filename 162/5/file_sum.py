# project-5a
# Author: Craig Sperlazza
# Date: 1/29/2020
# Description: This program takes a source file that contains a list of numbers
#     which are listed one number per line not a pythonic list).
#     This function will sum the values of the
#     numbers contained in the source file and write the sum to a
#     destination text file named sum.txt

def file_sum(source):
    """This function takes a source file that contains a list of numbers that
    are listed one number per line. This function will sum the values of the
    numbers contained in the source file and write the sum to a
    destination text file named sum.txt """
    sum_list = [] #This will be used to append each item in the source file
    sum_total = 0 #total sum of the numbers to send to destination file

    with open(source, 'r') as infile: #appends items from source file to sum_list
        for line in infile:
            sum_list.append(line.strip())
    #print(sum_list)

    with open('sum.txt', 'w') as outfile: #will sum and then write to destination
        for num in sum_list:
            sum_total = sum_total + float(num) #must convert str to float
        outfile.write(str(sum_total)) #must cast back to string prior to writing


