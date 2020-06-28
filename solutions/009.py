"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2


# m^2 + mn = 500

# m = -n/2 +/- sqrt( n^2 + 2000 ) / 2

# Find smallest solution of above where 
# sqrt( n^2 + 2000 ) is an integer

import math

def run() -> int:
    i = 1

    while True:
        val = math.sqrt( i**2 + 2000 )
        
        if math.floor( val ) == val:
            
            break
            
        i += 1
        
    n = i

    m = ( -n + val ) // 2

    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2

    return int( a*b*c )

if __name__ == '__main__':
    print( run())