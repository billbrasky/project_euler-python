"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

from math import sqrt

def divisors(n):
    if n == 1: return n
    s = 0
    end = int(sqrt(n))+1
    for i in xrange(1, end):
        if n%i == 0:
            if n/i == i:
                s += i
            else:
                s += i+n/i
    return s-n

abundNum = [0]
res = 0

numList = [1 for i in xrange(28123)]
for n in xrange(1,len(numList)):
    if numList[n] == 0:
        continue
    if divisors(n) > n:
        abundNum += [n]
        abundNum = [n+x for x in abundNum]
        k = n
        while k < len(numList):
            numList[k] = 0
            k +=k
        


#print len(abundNum)
#print numList
print abundNum[:50]
abundSum = {0: 1}
c = 1
for i in xrange(len(abundNum)):
    j = i
    for i in xrange(len(abundNum)):
        sval = abundNum[i]+abundNum[j]
        #print sval
        if sval > 28123:
            break
        if abundSum.get(sval, 0) == 1:
            abundSum.update({sval: 0})

res = 0
for i in xrange(28123):
    if abundSum.get(i, 0) == 1:
        res += i
    
print res