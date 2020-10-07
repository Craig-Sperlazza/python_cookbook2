'''
This code sample demonstrates splitting an input in half
at every step of a loop. We see this in things like binary search
or some kinds of sorts. We divide by half (immediately throw away half)
so the thing we are looping on is divided in each iteration---log growth
'''

from timethis import timethis
import time

@timethis
def split_in_two(i):
    while i > 1:
        i = i/2
        time.sleep(0.01) #We need to insert an arbitrary delay otherwise it is too fast

split_in_two(50)
split_in_two(100)
split_in_two(200)
split_in_two(400)
split_in_two(800)
split_in_two(1600)