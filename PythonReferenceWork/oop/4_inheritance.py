# corey shaffer
#
# video 4 of 6 OOP Python---inheritance
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

    def __str__(self):
        return f"The employee's information is: name = {self.first} {self.last}, salary = {self.salary}, and email = {self.email}"

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
        """
        self.salary = int(self.salary * self.raise_amount)


class Help_function_test(Employee):
    pass


class Manager(Employee):
    """Inherting from Employee but can pass in a list of employees set at default == none

    Args:
        Employee ([type]): [description]
    """

    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.full_name()}")


class Developer(Employee):
    """We want to inherit from Employee but also want to pass in their langauge and give them a higher raise

    Args:
        Employee ([type]): [description]
    """
    raise_amount = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


# method resolution order---class, class you inherited from, then built in object
# you can see this using the help method

# print(help(Help_function_test))

dev1 = Developer('Corey', 'Shaffer', 10000, 'Python')
dev2 = Developer('Tara', 'Black', 20000, 'Java')
emp1 = Employee('Craig', 'Prince', 10000)
mgr1 = Manager('Sue', "Jones", 200000, [dev1, emp1])

# print(dev1.salary)
# dev1.apply_raise()
# print(dev1.salary)

# print(emp1.salary)
# emp1.apply_raise()
# print(emp1.salary)

# print(dev1.prog_lang)
# print(dev1.email)

# print(dev2.prog_lang)
# print(dev2.email)

print(mgr1.full_name())
print(mgr1.email)
mgr1.print_emps()

print(f"Lets add an employee to {mgr1.full_name()}:")
mgr1.add_emp(dev2)
mgr1.print_emps()

print(f"Lets remove an employee from {mgr1.full_name()}:")
mgr1.remove_emp(dev1)
mgr1.print_emps()


# isinstance and issubclass methods

print(isinstance(mgr1, Manager))  # true
print(isinstance(mgr1, Employee))  # true
print(isinstance(mgr1, Developer))  # false

print(issubclass(Manager, Employee))  # true
print(isinstance(Manager, Developer))  # false
