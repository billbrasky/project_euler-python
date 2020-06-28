"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the 
right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# follows pascals triangle

from math import factorial

def run() -> int:

    n = 20
    return factorial( 2*n ) / ( factorial( n ))**2

if __name__ == "__main__":
    print( run())
