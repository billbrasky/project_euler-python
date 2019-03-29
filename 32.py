"""
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 
pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""

from functions import getfactors

def singlecounts( n, testlength = None ):
    
    s = str( n )
    if testlength is not None and len( s ) != testlength:
        return False
        
    if '0' in s:
        return False
    
    x = sum( [s.count( c ) for c in s] )

    return x == len( s )

res = 0
l = []
for n in range( 100, 10000 ):
    
    if not singlecounts( n ):
        continue

    factors = getfactors( n )
    
    for i in range( 0, len( factors ), 2):
        
        if i + 1 == len( factors ):
            factor1 = factor2 = factors[i]

        else:
            factor1, factor2 = factors[i:i+2]
        

        test = str( factor1 ) + str( factor2 ) + str( n )
        if not singlecounts( test, 9 ):
            continue
        
        else:
            l.append(( factor1, factor2, n ))
            res += n
            break
        
print( res )
