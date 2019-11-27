"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

from solutions.functions import getfactors

def run():
    counter = 1
    i = 3

    while True:

        if getfactors( i, primefactors = False, testprime = True ):
        
            counter += 1
        
        if counter == 10001:
        
            return i
            break

        i += 1


if __name__ == '__main__':
    print( run())
