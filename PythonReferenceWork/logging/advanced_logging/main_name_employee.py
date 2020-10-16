import logging

# logging.basicConfig(filename='/home/craig/Desktop/python_cookbook2/PythonReferenceWork/logging/advanced_logging/employee_test.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug('This is a log message')

class Employee:
    """Employee class for testing logging
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info(f"Created employee: {self.fullname} - {self.email}")
    
    def __str__(self):
        return f"The employee's name is {self.fullname} and their email is {self.email}"
    
    @property
    def email(self):
        return self.first + "." + self.last +"@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

if __name__ == "__main__":
    logging.basicConfig(filename='/home/craig/Desktop/python_cookbook2/PythonReferenceWork/logging/advanced_logging/employee_test.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.debug('This is a log message')

    emp1 = Employee("John", "Smith")
    emp2 = Employee("Katie", "Johnson")
    emp3 = Employee("Rhonda", "Jones")
else:
    print("Employee Imported")