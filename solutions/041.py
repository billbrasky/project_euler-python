"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also 
prime.

What is the largest n-digit pandigital prime that exists?
"""

from solutions.functions import getfactors
import itertools


m = 9

res = 0
while m > 1:
    
    p = itertools.permutations( range( 1, m + 1 ))
    
    for x in p:
        
        end = x[-1]
        
        if end % 2 == 0 or end % 5 == 0:
            continue

        x = [str( y ) for y in x ]
            
        n = int( ''.join( x ))
         
        prime = getfactors( n, testprime = True )
       
        if prime and n > res:
            res = n
    
    
    if res != 0:
        m = 0
    
    else:
        m -= 1

print( res )
