# project-5b
# Author: Craig Sperlazza
# Date: 1/29/2020
# Description: Program contains class named NobelData that reads a JSON file
# containing data on Nobel Prizes the class contains a method that allows
# the user to search that data by category and year. The method will return a
# list of all winners meeting the search criteria.

from typing import List, Optional
import json

class NobelData:
    """
    __init__: Creates a NobelData class that contains an init method that reads
    a json file that contains data on nobel prizes and allows a user to search
    that data.

    Method: This class also has a method named search_nobel that takes as
    parameters a year (string format) and a category. The 5 categories are:
    "chemistry", "economics", "literature", "peace", "physics", and "medicine".

    Return: The function returns a sorted list of the surnames for the winner(s)
    in that category for that year. Up to three people can
    share the prize any given year."""


    def __init__(self, file_name = "nobels.json") -> None:
        """init method that reads a json file that contains data on nobel prizes
         and allows a user to search that data"""
        self.file_name = file_name
        with open('nobels.json', 'r') as infile:
            self.nobels = json.load(infile)

    def __str__(self) -> str:
        return ''.join([
            'NobelItem(',
            f'file_name={self.file_name}, ',
            ')'
        ])

    def search_nobel(self, year: str, category: str) -> List[str]:
        """The search_nobel method takes a year (as a string) and a category as
        parameters. The 5 categories possible are: "chemistry", "economics",
        "literature", "peace", "physics", and "medicine".
        Search_nobel method returns a list of the surnames of the winners for
        the inputed year and category (sorted alphabetically)

        Note on the lists employed: This method makes use of three lists.
        1. winners_lst which takes the parsed JSON  file data and stores the
        winners that meet the inputed criteria.
        2. intermediate list (see below for explanation) that serves merely as
        a sorting ground.
        3. final_list which will hold the surnames. It will be returned sorted

        """
        winners_lst = []
        length_of_values = len(self.nobels["prizes"]) #number key:prizes values
        final_lst = []

        #This for loop iterates through the JSON file data and pulls out entries
        #matching the year and category inputed. It appends data to winners_lst
        for winner in range(0, length_of_values):
            if self.nobels['prizes'][winner]["year"] == year and self.nobels['prizes'][winner]["category"] == category:
                winners_lst.append(self.nobels['prizes'][winner]["laureates"])

        #The above function creates a list of lists. This strips away the extra,
        #empty portion of the list.
        int_lst = winners_lst[0]
        length_of_int = len(int_lst)

        #pulls out the value for the key surname and appends it to final_lst
        for name in range(0, length_of_int):
            final_lst.append(int_lst[name]["surname"])

        #print(final_lst)
        final_lst.sort()

        #print(final_lst)
        return(final_lst)

"""
##########TESTING###############################################################
nd = NobelData()
nd.search_nobel("2001", "economics")
nd.search_nobel("2019", "economics")
nd.search_nobel("2019", "peace")
nd.search_nobel("2019", "medicine")
"""

"""
################################################################################

THE BELOW IS JUST MY STEP BY STEP PARSING OF THE JSON FILE TO UNDERSTAND HOW TO 
BETTER RETRIEVE THE DATA FOR THE FINAL USE IN THE METHOD. 


for i in self.nobels:
    print(i) # prints "prizes" (parent key)
    print(self.nobels[i][0]) #returns first categories winners (shared among 3)
    print(self.nobels[i][0]["year"]) #returns key value for year 2019 at 0th position
    print(self.nobels[i][0]["category"]) #returns key value chemistry for oth position
    
    # print statement below returns list of dictionary items
    # contains each winner if more than one
    # this list contains a dictionary
    # 0 entry key is id, 1st entry key is firstname,
    # 2nd entry key is surname which is what we need
    print(self.nobels[i][0]["laureates"])

#Loop through using range with i = integer to update the above values each loop
length = len(self.nobels)
print(length) #1 (only counting prizes)
length_of_values = len(self.nobels["prizes"])
print(length_of_values) #646 dictionary objects in the list
#note that it is a dictionary key(prizes):value(list)
#that values list---- contains 646 dictionary objects embedded as above

#for i in range(0, length_of_values):
    #print(i) #prints 0-645

#for i in range (0, length_of_values):
    #print(self.nobels['prizes'][i]) #printed out every value (i.e. 646 dictionary objects)


######The following two will be used for search conditionals##############
for i in range (0, length_of_values):
    print(self.nobels['prizes'][i]["year"])

    #does print years 2019-1901. 2019 has 6 entries. JSON data supports this.
    #retreiving years correctly

for i in range(0, length_of_values):
    print(self.nobels['prizes'][i]["category"])
    #appears to retrieve each category
    # "chemistry", "economics", "literature", "peace", "physics",
    # and "medicine" correctly and (apparently) just repeatedly returns
    # it year by year


######The following holds the data to retrieve##############
temp_list = []
#for i in range(0, length_of_values):
    #print(self.nobels['prizes'][i]["laureates"])
    # returns a list of each laureate. This list contains a dictionary
    # with the following relevant keys:
    # 0 = "id", 1 = "firstname", 2 = "surname"


#for i in range(0, length_of_values):
    #print(self.nobels['prizes'][i]["laureates"][0])
    #useless just prints the 0th item, which is the entire list

#for i in range(0, length_of_values):
    #print(self.nobels['prizes'][i]["laureates"][0]['surname'])
    #DOES NOT WORK, prints some surnames not all---not really sure


#for i in range(0, length_of_values):
    #print(self.nobels['prizes'][i]["laureates"]["surname"])
    #WILL NOT WORK, WE NEED A INDEX NOT A STR

#So we need to loop back through the inside list (the laureate list)
#for i in range(0, length_of_values):
    #print(self.nobels['prizes'][i]["laureates"])
    #winners_lst = self.nobels["prizes"][i]["laureates"]
#for i in winners_lst:
    #print(i)

"""


