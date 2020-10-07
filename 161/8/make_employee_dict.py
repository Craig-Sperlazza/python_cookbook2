# project-8c
# Author: Craig Sperlazza
# Date: 11/7/2019
# Description: An Employee class that has four data members to create
# Employee objects and a separate function that instantiates Employee objects
# and adds them to a dictionary

class Employee:
    """Creates an Employee class that contains four data members:
     name, ID Number, salary, and email address"""

    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address


def make_employee_dict(list_name, list_id, list_salary, list_email):
    """Creates an Employee object from 4 lists and adds each employee instance
    to a dictionary, with the Employee ID as the key and the employee object
    as the value (employee object contains the name, id, salary and email).
    """
    employee_dict = {}  #Empty list to hold the Employee objects
    count = 0  #Count will be used in for loop to traverse each list

    for i in list_id:
        employee_dict[i] = Employee((list_name[count]), list_id[count],
                                    list_salary[count],  list_email[count])
        count = count + 1

    return employee_dict



