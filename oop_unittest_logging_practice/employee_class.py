from typing import List, Tuple, Dict, Sequence, Optional
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('/home/craig/Desktop/python_cookbook2/oop_unittest_logging_practice/employee_log.txt')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a log message')

class Employee:

    pay_raise = 1.05

    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_employees += 1

        logger.info(f"Created Employee {self.first}, {self.last}, {self.pay}, {self.full_name}, {self.email} \n"
                    f"The total number of employees is now {Employee.num_employees}")

    def __repr__(self):
        return f"Employee {self.first}, {self.last}, {self.pay}"

    def __str__(self):
        return f" The Employee's name is {self.full_name} and their pay is {self.pay} and their email is {self.email}"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @classmethod
    def employee_count(cls):
        return {f"The number of employees is {cls.num_employees}"}

    @classmethod
    def set_raise(cls, amt):
        Employee.pay_raise = amt

    def give_raise(self):
        self.pay = int(self.pay * self.pay_raise)





if __name__ == '__main__':
    emp1 = Employee("John", "Smith", 100000)
    emp2 = Employee("Katie", "Johnson", 150000)
    emp3 = Employee("Rhonda", "Jones", 200000)
    logger.info(emp1)
    logger.info(Employee.employee_count())

    print(emp3.pay)
    print(Employee.pay_raise)
    emp3.give_raise()
    print(emp3.pay)
    Employee.set_raise(1.10)
    print(emp3.pay_raise)
    emp3.give_raise()
    print(emp3.pay)


else:
    print("Employee Imported")