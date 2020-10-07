from typing import List, Optional


class Dog:
    """Dog class for basic practice
    """

    def __init__(self, breed: str, name: str, age: int):
        self.breed = breed
        self.name = name
        self.age = age

    def __str__(self):
        return f"The dogs breed is {self.breed}, name is {self.name}, and its age is {self.age}"

    def __repr__(self):
        return f"The dogs breed is {self.breed}, name is {self.name}, and its age is {self.age}"

    def bark(self) -> str:
        print(f"{self.name} says WOOF")

    def birthday(self) -> int:
        self.age += 1
        return self.age


Bell = Dog("Collie", "Bella", 15)
Diablo = Dog("Pitty", "Bodhi", 1)

print(Bell)
print(Bell.age)
Bell.birthday()
print(Bell.age)
Bell.bark()
