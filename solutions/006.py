""" 
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""


def run() -> int:
    n = 100

    squareofsum = ( n // 2 * ( 1 + n ))**2

    sumofsquares = n * ( n + 1 ) * ( 2 * n + 1 ) // 6


    return squareofsum - sumofsquares


if __name__ == '__main__':
    print( run())
