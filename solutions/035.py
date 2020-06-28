"""
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 
79, and 97.

How many circular primes are there below one million?
"""


from solutions.functions import getprimes
import re

def rotate( n ):
    
    
    a = [x for x in str( n )]

    l = len( a )

    
    res = [ [a[(i+k)%l] for k in range( l )] for i in range( l )]
    
    res = [int( ''.join( x )) for x in res ]
    
    return res
    


primes = getprimes( 10**6 )


counter = 0

for prime in primes:

    if prime < 10:
        counter += 1
        continue

    if re.search( r'[024568]', str( prime )) is not None:
        continue

    isotopes = rotate( prime )
    
    moveon = False
    for isotope in isotopes:
        
        if isotope < prime or isotope not in primes:
            moveon = True
            break
    
    if not moveon:
        counter += len( set( isotopes ))
        
print( counter )
