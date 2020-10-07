# corey shaffer
#
# video 5 of 6 OOP Python---Dunder Methods
# we will make a Developer and Manager subclasses which both inherit the basics form Employee

# https://github.com/pallets/werkzeug/blob/master/src/werkzeug/exceptions.py   see this link for a good example of subclasses

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
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def __repr__(self):
        """RULE OF THUMB FOR REPR----use it to print something that would recreate the object

        Returns:
            [type]: [description]
        """
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.salary)

    def __str__(self):
        return f"The employee's information is: name = {self.first} {self.last}, salary = {self.salary}, and email = {self.email}"

    def __add__(self, other):
        """Contrived example that adds the salary of two employee objects together.

        """
        return int(self.salary) + int(other.salary)

    def __len__(self):
        """We want it to return total chacters in their full name"""
        return len(self.full_name())

    def full_name(self):
        """

        Returns:
            Employee's First Name and Last Name
        """
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """applies a raise to an employee using the global variable raise_amount
        """
        self.salary = int(self.salary * self.raise_amount)


# if you have a __str__ it will be used
emp1 = Employee("Craig", "Sperlazza", "33333")
emp2 = Employee("Crane", "Sper", "44444")

# can always still call __repr__ directly
print(repr(emp1))
print(emp1)

# __add__
print(Employee.__add__(emp1, emp2))

# __len__
print(len(emp1))
