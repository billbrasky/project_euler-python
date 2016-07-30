"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

m = 999
k = 0

while k < 899:
    t = 0
    while t < (k/2+1): 
        test_string = str((m-k/2+t)*(m-k/2-t))
        if k%2 != 0:
            test_string = str((m-k/2+t)*(m-k/2-t+1))        
    
        front = test_string[:len(test_string)/2]
        back = test_string[:len(test_string)/2:-1]
        if len(test_string) == 6:
            back = test_string[:len(test_string)/2-1:-1]

        if front == back:
            print test_string
            t = -1
            k = 899

        t += 1
    k += 1
