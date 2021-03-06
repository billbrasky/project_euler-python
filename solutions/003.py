
""" 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from util.functions import getfactors

def run() -> int:

    m = 600851475143

    return max( getfactors( n = m ))

if __name__ == '__main__':
    print( run())