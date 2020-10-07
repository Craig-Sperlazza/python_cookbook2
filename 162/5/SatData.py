# project-5c
# Author: Craig Sperlazza
# Date: 1/29/2020
# Description: Contains a class named SatData that reads a JSON file containing
# data on 2010 SAT results for New York City and contains a method to write
# the data to a text file in CSV (comma-separated values) format.

from typing import List, Optional
import json

class SatData:
    """
    __init__: Creates a SatData class that contains an init method that reads
    a json file ("sat.json": file contains 2010 SAT results for New York City)

    Method: This class also has a method named save_as_csv that
    takes as a parameter a list of DBNs (district bureau numbers)
    and saves as a CSV file a table with only the rows corresponding to the DBNs
    in the list (and also the row of column headers)."""

    def __init__(self, file_name = "sat.json") -> None:
        """init method that reads a json file named sat.json that contains data
        2010 SAT results for New York City"""
        self.file_name = file_name
        with open('sat.json', 'r') as infile:
            self.sat = json.load(infile)

    def __str__(self) -> str:
        return ''.join([
            'SATItem(',
            f'file_name={self.file_name}, ',
            ')'
        ])

    def save_as_csv(self, dbn_lst: List[str]) -> None:
        """The save_as_csv method: takes as a parameter a list of DBNs
        (district bureau numbers) and saves as a CSV file a table with only
        the rows corresponding to the DBNs in the list
        (and also the row of column headers)."""

        length_of_values = len(self.sat["data"])
        length_of_dbn = len(dbn_lst)
        matching_dbn_lst = []

        ###TEST PRINT################
        #print(length_of_values)
        #for i in self.sat["data"]:
            #print(i)
        #for i in dbn_lst:
            #print(i) #prints dbn


        # This for loop iterates through the JSON file data and pulls out entries
        # matching the year and category inputed. It appends data to winners_lst
        for sat_taker in range(0, length_of_values):
            for dbn in dbn_lst:
                if self.sat["data"][sat_taker][8] == dbn:
                    matching_dbn_lst.append(self.sat["data"][sat_taker][8:14])

        #print(matching_dbn_lst)

        length_matching_dbn_lst = (len(matching_dbn_lst))

        #print(length_matching_dbn_lst)

        matching_dbn_lst.sort() #sorts dbns

        #new_list used to flatten out list to convert to strings for csv
        new_lst = []

        for person in matching_dbn_lst:
            for element in person:
                new_lst.append(element) #flattens out the nested list to a list

        #print(new_lst)

        i = 6
        while i < len(new_lst):
           new_lst.insert(i, '\n') #add line breaks to flattened list where needed
           i += 7

        #print(new_lst)

        #Will write the headers to the csv file
        with open('output.csv', 'w') as outfile:
            outfile.write("DBN" + ',')
            outfile.write("School Name" + ',')
            outfile.write("Number of Test Takers" + ',')
            outfile.write("Critical Reading Mean" + ',')
            outfile.write("Mathematics Mean" + ',')
            outfile.write("Writing Mean" + '\n')

        #will write the list data to the csv file in appropriate columns
        with open('output.csv', 'a') as outfile:
            for i in range(0, len(new_lst)):
                if new_lst[i] == "\n": #adds in line break
                    outfile.write(new_lst[i])
                elif new_lst[i] == None: #accounts for blank entries
                    outfile.write(" ")
                #must account for end of lines:
                elif i == 5 or i == 12 or i == 19 or i == 26 or i == 33 or i == 40:
                    outfile.write(new_lst[i])
                elif i == 47 or i == 54 or i == 61 or i == 68 or i == 75 or i == 82:
                    outfile.write(new_lst[i])
                elif i == 89 or i == 96 or i == 103 or i == 110 or i == 117 or i == 124:
                    outfile.write(new_lst[i])
                elif i == 131 or i == 138 or i == 145 or i == 152 or i == 159 or i == 166:
                    outfile.write(new_lst[i])
                elif i == 173 or i == 180 or i == 187 or i == 194 or i == 201 or i == 208:
                    outfile.write(new_lst[i])
                elif i == 215 or i == 222 or i == 229 or i == 236 or i == 243 or i == 250:
                    outfile.write(new_lst[i])
                elif i == 257 or i == 263 or i == 270 or i == 277 or i == 284 or i == 291:
                    outfile.write(new_lst[i])
                elif i == 298 or i == 305 or i == 312 or i == 319 or i == 326 or i == 333:
                    outfile.write(new_lst[i])
                elif i == 340 or i == 347 or i == 354 or i == 361 or i == 368 or i == 375:
                    outfile.write(new_lst[i])
                elif i == 382 or i == 389 or i == 396 or i == 403 or i == 410 or i == 417:
                    outfile.write(new_lst[i])
                elif i == 424 or i == 431 or i == 438 or i == 445 or i == 452 or i == 459:
                    outfile.write(new_lst[i])
                elif i == 466 or i == 473 or i == 480 or i == 487 or i == 494 or i == 501:
                    outfile.write(new_lst[i])
                elif i == 508 or i == 515 or i == 522 or i == 529 or i == 536 or i == 543 or i == 550:
                    outfile.write(new_lst[i])
                else:
                    outfile.write(new_lst[i] + ",")

"""
sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418", "01M509"]
sd.save_as_csv(dbns)
"""


