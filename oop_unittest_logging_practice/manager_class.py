from typing import List, Tuple, Dict, Sequence, Optional
import logging
from employee_class import Employee
from developer_class import Developer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('/home/craig/Desktop/python_cookbook2/oop_unittest_logging_practice/manager_log.txt')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a log message')

class Manager(Employee):
    pay_raise = 1.50

    def __init__(self, first, last, pay, subordinates=None):
        super().__init__(first, last, pay)
        if subordinates == None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

        Employee.num_employees += 1

        logger.info(
            f"Created Manager {self.first}, {self.last}, {self.pay}, {self.full_name}, {self.email}\n"
            f"The total number of employees is now {Employee.num_employees}")

    def add_emp(self, emp):
        if emp not in self.subordinates:
            self.subordinates.append(emp)

    def remove_emp(self, emp):
        if emp in self.subordinates:
            self.subordinates.remove(emp)

    def print_emps(self):
        for emp in self.subordinates:
            print(f"{emp.full_name}")

if __name__ == "__main__":
    dev1 = Developer('Corey', 'Shaffer', 10000, 'Python')
    dev2 = Developer('Tara', 'Black', 20000, 'Java')
    emp1 = Employee('Craig', 'Prince', 10000)
    mgr1 = Manager('Sue', "Jones", 200000, [dev1, emp1])
    logger.info(emp1)
    logger.info(dev1)
    logger.info(dev2)
    logger.info(mgr1)
    logger.info(Employee.employee_count())

    print(mgr1.full_name)
    print(mgr1.email)
    mgr1.print_emps()
    print("_____________________")

    print(f"Lets add an employee to {mgr1.full_name}:")
    mgr1.add_emp(dev2)
    mgr1.print_emps()

    print("_____________________")
    print(f"Lets remove an employee from {mgr1.full_name}:")
    mgr1.remove_emp(dev1)
    mgr1.print_emps()
