import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/unittest_module/employee_log.txt')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a log message')


class Employee:
    """Employee class for testing logging
    """
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        logger.info(f"Created employee: {self.fullname} - {self.email} - {self.pay}")
    
    def __str__(self):
        return f"The employee's name is {self.fullname} and their email is {self.email} and their pay is {self.pay}"
    
    @property
    def email(self):
        return self.first + "." + self.last +"@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    ##### Mocking ##############################
    """ When we do a test that relies on something else, such as a website being up, we want to mock it 
    so we dont think our code is failing because another resource that is out of our control is failing"""
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

if __name__ == "__main__":
    emp1 = Employee("John", "Smith", 100000)
    emp2 = Employee("Katie", "Johnson", 150000)
    emp3 = Employee("Rhonda", "Jones", 200000)
else:
    print("Employee Imported")
