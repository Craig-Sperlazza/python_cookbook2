# project-5b

# Author: Craig Sperlazza
# Date: 10/23/2019
# Description: Create a class to represent taxicab objects for which the user
# can get and change the current position of the taxi via x and y coordinates)
# and retrieve the current odometer reading (total distance) for the taxi


class Taxicab:
    """Represents taxicab objects that tracks current position and
    total distance travelled for a taxicab object"""


    def __init__(self, x_coord, y_coord):
        """Initializes the x-coordinate, y-coordinate, and the odometer"""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0


    def get_x_coord(self):
        """Returns the current x-coord"""
        return self._x_coord


    def get_y_coord(self):
        """Returns the current y-coord"""
        return self._y_coord


    def get_odometer(self):
        """Returns the current odometer value (i.e. total distance travelled)"""
        return self._odometer


    def move_x(self, move_x):
        """Moves the x-coord  and adds the distance to the odometer"""
        self._odometer = self._odometer + abs((move_x))
        self._x_coord += move_x


    def move_y(self, move_y):
        """Moves the y-coord and adds the distance to the odometer"""
        self._odometer = self._odometer + abs((move_y))
        self._y_coord += move_y

"""
cab = Taxicab(10, -10)

print(cab.get_x_coord())
print(cab.get_y_coord())
print(cab.get_odometer())

cab.move_x(3)
cab.move_y(-4)
cab.move_x(-100)
cab.move_y(320)


print(cab.get_x_coord())
print(cab.get_y_coord())
print(cab.get_odometer())
"""