# corey shaffer
#
# video 6 of 6 OOP Python---getter and setter and delete decorators

# @property decorator---allows us to define a method but access it liek a property


from typing import List, Tuple, Dict, Sequence, Optional
import datetime


class Employee:
    """Employee Class: receives a first name, last name, salary
        creates an employee email
    """

    # Class variables
    raise_amount = 1.04  # 4% annual raise for all employees
    num_of_employees = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        # we are removing email and creating it via a method and decorating it with @property
        # self.email = first + '.' + last + '@company.com'

    def __repr__(self):
        """RULE OF THUMB FOR REPR----use it to print something that would recreate the object

        Returns:
            [type]: [description]
        """
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.salary)

    def __str__(self):
        return f"The employee's information is: name = {self.first} {self.last}, salary = {self.salary}, and email = {self.email}"

    # BECAUSE WE USED THE PROPERTY DECORATOR WE CAN CALL fullname METHOD LIKE A PROPERTY AND NOT A METHOD
    # print(emp1.fullname)
    @property
    def fullname(self):
        """

        Returns:
            Employee's First Name and Last Name
        """
        return f"{self.first} {self.last}"

    # BECAUSE WE USED THE PROPERTY DECORATOR WE CAN CALL EMAIL METHOD LIKE A PROPERTY AND NOT A METHOD
    # print(emp1.email)

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    # Setter decorator allows us change properties
    # name for the setter is the property we want to set
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # deleter property allows us delete
    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first = None
        self.last = None


emp1 = Employee("Craig", "Sperlazza", "33333")
emp2 = Employee("Crane", "Sper", "44444")

emp1.first = "James"

# BECAUSE WE USED THE PROPERTY DECORATOR WE CAN CALL EMAIL METHOD LIKE A PROPERTY AND NOT A METHOD
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

# using the setter function we can update a full name (for example) by implicitly changing first and last
emp1.fullname = 'Reggie Bush'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

# using the delter function we can delete an attribute
del emp1.fullname
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
