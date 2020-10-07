class Circle:
    """generic circle class
        give it a generic radius of 1 unless specified
    """

    def __init__(self, radius: float = 1.0):
        self.radius: float = radius
        self.pi: float = 3.14

    def __str__(self):
        return f"This circle has a radius of {self.radius}"

    def __repr__(self):
        return f"This circle has a radius of {self.radius}"

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius) -> None:
        self.radius = new_radius

    def area(self) -> float:
        area = self.pi * (self.radius ** 2)
        print(f"The area of a circle with a radius of {self.radius} is {area}")


big = Circle(5.0)
print(big)
print(big.area())
print(big.radius)
print(big.get_radius())
big.set_radius(10)
big.area()
