"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# takes longer than 2 seconds
N = 2000000
numbers = [0]+[1 for x in xrange(N-1)]
res = 0
for k in xrange(N):
    if numbers[k] == 1:
        res += k+1
        for j in xrange(2*(k+1), N+1, (k+1)):
            numbers[j-1] = 0

print res
