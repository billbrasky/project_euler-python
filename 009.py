"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

m = 1000

c = m/2

# For each iteration of c steping down
# b steps down from m-(a+c) and
# a steps up from 1

# b_stop removes rendundancies within the second while loop
# However, there are still many results being checked multiple times
# a = 1, b = 5, c = 4, for example gets checked twice...
while c > 0:
    a = 1
    b = m - (a+c)
    b_stop = b/2
    while b > b_stop:
        if a**2+b**2 == c**2:
            print a*b*c

        a += 1
        b -= 1
    c -= 1

