class NegativeParameterError(Exception):
    pass

class RegularProject():
    """Represents a construction project"""

    def __init__(self, hours, materials, transportation):
        """returns a RegularProject object"""
        if hours < 0 or materials < 0 or transportation < 0:
            raise NegativeParameterError
        self._hours = hours
        self._materials = materials
        self._transportation = transportation

    def bill_amount(self):
        return self._hours * 80 + self._materials + self._transportation

def main():
    try:
        obj_1 = RegularProject(210, 600, 250)
        print(obj_1.bill_amount())
    except NegativeParameterError:
        print("One or more parameters are negative")

if __name__ == '__main__':
    main()