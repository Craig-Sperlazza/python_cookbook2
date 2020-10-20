from typing import List, Tuple, Dict, Sequence, Optional
import logging
from employee_class import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('/home/craig/Desktop/python_cookbook2/oop_unittest_logging_practice/developer_log.txt')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a log message')

class Developer(Employee):
    pay_raise = 1.20
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

        Employee.num_employees += 1

        logger.info(f"Created Developer {self.first}, {self.last}, {self.pay}, {self.full_name}, {self.email}, {self.prog_lang} \n"
                    f"The total number of employees is now {Employee.num_employees}")

    def __repr__(self):
        return f"Developer {self.first}, {self.last}, {self.pay}"

    def __str__(self):
        return f" The Developer's name is {self.full_name} and their pay is {self.pay} and their email is {self.email}"


if __name__ == "__main__":
    emp1 = Employee("John", "Smith", 100000)
    dev1 = Developer("Katie", "Johnson", 150000, "python")
    emp3 = Employee("Rhonda", "Jones", 200000)
    logger.info(emp1)
    logger.info(Employee.employee_count())

    print(emp3.pay)
    print(Employee.pay_raise)
    emp3.give_raise()
    print(emp3.pay)
    Employee.set_raise(1.10)

    print(dev1.pay)
    print(Employee.pay_raise)
    dev1.give_raise()
    print(dev1.pay)
    Employee.set_raise(1.11)
    print(dev1.pay_raise)
    dev1.give_raise()
    print(dev1.pay)

    print(emp3.pay_raise)
    emp3.give_raise()
    print(emp3.pay)

else:
    print("Developer Imported")


