"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

pdees = {}
k = 2
while k < 21:
    if len(pdees) == 0:
        pdees.update({k:1})
    else:
        k_temp = k
        for pdiv in pdees.keys():
            counter = 0
            while k_temp % pdiv == 0:
                counter += 1
                k_temp = k_temp/pdiv

            if counter > pdees[pdiv]:
                pdees.update({pdiv: counter})

            if k_temp == 1:
                break
            elif pdees.keys().index(pdiv) == len(pdees.keys())-1:
                pdees.update({k_temp: 1})
    k += 1

res = 1
for pdiv in pdees.keys():
    res *= pdiv**pdees[pdiv]
print res
