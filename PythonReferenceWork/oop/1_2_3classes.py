# corey shaffer
#
# video 1 of 6 OOP Python---setting up a basic class
#
# video 2 of 6: class variables to share amongst instances
# #####class variable example is the employee annual raise where everyone's is the same 4%
#
# video 3 of 6: class methods (including alternative constructor) and static methods
# regular method takes an instance of the class in first (self)
# class method takes the class itself by using @classmethod decorator

# regular methods automatically pass instance (self) as first argument
# class methods automatically pass class (cls) as first argument
# static methods DO NOT pass anything automatically

from typing import List, Tuple, Dict, Sequence, Optional
import datetime


class Employee:
    """Employee Class: receives a first name, last name, salary
        creates an employee email
    """

    # Class variables----data you want shared between all employees---same for all
    raise_amount = 1.04  # 4% annual raise for all employees
    num_of_employees = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'

        # here we dont use self since it has nothing to do with an instance but the class itself
        Employee.num_of_employees += 1

    def __str__(self):
        return f"The employee's information is: name = {self.first} {self.last}, salary = {self.salary}, and email = {self.email}"

    # remember this is wrong use of repr---- should be Employee(first, last, salary)
    def __repr__(self):
        return f"The employee's information is: name = {self.first} {self.last}, salary = {self.salary}, and email = {self.email}"

    def full_name(self):
        """

        Returns:
            Employee's First Name and Last Name
        """
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """applies a raise to an employee using the global variable raise_amount
        we use self.raise_amount because you can then change it for any given employee instance if you so choose
        If we used Employee.raise_amount instead you couldn't chang eit for indiviudal employees
        Technically you cna chang eit into their namespace but the formula wouldnt care. 
        """
        self.salary = int(self.salary * self.raise_amount)

    # class methods---methods that operate on the whole class
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternative constructor
    # use case example: where our employee information comes in a string with info seperate by '-'
    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    # static methods---dont take instance or class as first argument
    # a static method should be used if you do not use the instance or the class in the method, such as below
    @staticmethod
    def is_work_day(day):
        """returns true if it is a workday. 

        Args:
            day (int): by python built in method .weekday where 0 is Monday, 6 is Sunday, etc.
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Craig', 'Sperlazza', 50000)
emp_2 = Employee('John', 'Smith', 60000)

print(emp_1)
print(emp_2.email)
print(emp_1.full_name())

print(Employee.full_name(emp_2))

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)


# __dict__ method
print(emp_1.__dict__)
# print(Employee.__dict__)

# class variable
print(Employee.num_of_employees)

# class method
# note that if you change the global variable for an instance it only applies to that instance
emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# but if you use the class method it changes the class
# Notice the class method does not override the instance amount we set above
Employee.set_raise_amount(1.08)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# alternative constructor
alt_emp_1_str = "John-Doe-40000"
alt_emp_2_str = "Sally-Mae-65000"

alt_emp_1 = Employee.from_string(alt_emp_1_str)
print(alt_emp_1)


# static method (uses datetime module)
my_date = datetime.date(2016, 7, 10)
print(Employee.is_work_day(my_date))
