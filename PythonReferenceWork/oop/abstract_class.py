from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    # class variables
    year_raise = 1.03

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"
    
    def curr_pay(self):
        return self.pay
    
    @classmethod
    def change_raise(cls, new_raise):
        cls.year_raise = new_raise

    @abstractmethod
    def give_raise(self):
        pass



class Developer(Employee):

    year_raise = 1.10

    def __init__(self, fname, lname, pay, language):
        super().__init__(fname, lname, pay)
        self.language = language
    
    def __str__(self):
        return f"This employee's name is {self.fname} {self.lname}, their programming language is {self.language}, and their pay is {self.pay}"
    
    def give_raise(self):
        self.pay = int(self.pay * self.year_raise)


if __name__ == '__main__':
    dev1 = Developer("Craig", "Sperlazza", 10000, 'python')
    print(dev1)
    print(dev1.pay)
    dev1.give_raise()
    print(dev1.pay)
    print(dev1.email())
