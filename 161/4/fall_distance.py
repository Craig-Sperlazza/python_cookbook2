# project-4a

# Author: Craig Sperlazza
# Date: 10/13/2019
# Description: Creates a function that takes the fall time of an object and returns the distance (in meters) the object has fallen

def fall_distance(time):
    """Takes a time value and returns the total fall distance for that time value"""
    distance = .5 * 9.8 * (time**2)
    return distance

