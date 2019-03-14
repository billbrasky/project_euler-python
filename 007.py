"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from math import log

# Determines how big N needs to be. This is 
# based on the number of primes required.
N = 1000
while N/log(N) < 10001:
    N *= 10

prime_counter = 0
numbers = [0]+[1 for i in xrange(N-1)]

for k in xrange(1,N+1):
    if numbers[k-1] == 1:
        prime_counter +=1
        for j in xrange(2*k, N, k):
            numbers[j-1] = 0

    if prime_counter == 10001:
        break
        
print k