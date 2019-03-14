"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

from functions import getfactors

counter = 0

i = 3

primes = []

while True:

	if getfactors( i, prime = True ) == []:
	
		counter += 1
	
	if counter == 10000:
	
		print( i )
		break

	i += 2

