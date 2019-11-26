"""
A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 1 
+ 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than 
this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
"""

from functions import getfactors
import time

start = time.time()

m = 28123

data = [0]+[1]*(m-1) + [0]
abunds = []
for i in range( 12, m+1 ):
    if data[i] == 0:
        abunds.append( i )
        continue
        
    s = sum( getfactors( i )) - i
    
    if s > i:
        test = i + i
        while test <= m:
            data[test] = 0
            test += i
               
        abunds.append( i )

for x in abunds:
    for y in abunds:
        r = x + y
        
        if r < m:
            data[r] = 0
        


res = 0
for i in range( len( data )):
    if data[i] == 1:
#        print( i )
        res += i
print( res )
        
print( time.time() - start )
    
    
