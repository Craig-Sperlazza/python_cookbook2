# project-4b
# Author: Craig Sperlazza
# Date: 1/16/2020
# Description: This program creates a Box class that initializes three members:
# the length, width and height of a Box. The Box class also has a method named
# volume that returns the volume of the Box. There is a separate function named
# box_sort (not part of the Box class) that uses insertion sort to sort the
# list of Box objects from greatest volume to least volume.

from typing import List, Optional

class Box:
    """Creates a Box class that contains three data members:
    the length, width, and height of a box.
    Box Class also has get and set methods for all 3 data members
    Box class has a method named volume that returns the volume of the Box"""

    def __init__(self, length: int, width: int, height: int) -> None:
        """Initializes 3 data members from input: length, width, height of
        a proposed Box object."""
        self.length: int = length
        self.width: int = width
        self.height: int = height
        #self.volume: int = 0

    def __str__(self) -> str:
        return ''.join([
            'Box(',
            f'length={self.length}, ',
            f'width={self.width}, ',
            f'height={self.height}, ',
            ')'
        ])

    def volume(self) -> int:
        """returns the volume of the box object. The formular for volume is
        length * width * height"""
        volume = self.length * self.width * self.height
        return volume

def box_sort(box_lst):
    """This function takes a list of Box Objects and uses insertion sort
    to sort the list of Box objects from greatest volume to least volume. It
    then returns the list sorted """
    for index in range(1, len(box_lst)):
        # element to be compared
        box_value = box_lst[index]
        pos = index - 1

        # comparing the current element with the sorted portion and swapping
        # using the < will sort it descending
        while pos >= 0 and box_lst[pos].volume() < box_value.volume():
            box_lst[pos + 1] = box_lst[pos]
            pos -= 1
        box_lst[pos + 1] = box_value
    return box_lst


"""
########TESTING################################################################
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
b4 = Box(2.0, 3.0, 2.0)
box_list = [b1, b2, b3, b4]
print(box_sort(box_list))


print('==== Begin Box List ====')
for p in range(len(box_list)):
    print(box_list[p].volume())
print('==== End Box List ====')
"""
