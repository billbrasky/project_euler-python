"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


m = 600851475143

prime_divisors = [2]

x = 3
while x <= m:
    if m%x == 0:
        m = m/x
        for p in prime_divisors:
            if x%p == 0:
                break
            elif prime_divisors.index(p) == len(prime_divisors)-1:
                prime_divisors.append(x)
    x += 1
        
print prime_divisors[-1]