""" 
The number 3797 has an interesting property. Being prime itself, it is possible to 
continuously remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 
3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# cannot have any even digits

import re 
from functions import getfactors

n = 10
counter = 0
res = 0
checked = {}
while True:
    n += 1

    s = str( n )

    regex = r'(\d+[02468]|' \
            r'^(3[39]+|1|9|\d+5)|' \
            r'(1|9|[39]+3)$)'

    if re.search( regex, s ) is not None:
        continue
    
    prime = getfactors( n, testprime = True )

    if not prime:
        continue

    moveon = False
#    digitsum = sum( [int( x ) for x in s] )
    lrs = 0
    rrs = 0
    for i in range( len( s ) - 1 ):
        lrs += int( s[i] )
        rrs += int( s[-i - 1 ] )
        
        left = s[:i+1]
        right = s[len( s ) - i - 1:]
        
        if lrs % 9 == 0 or rrs % 9 == 0:
#                print( s )
                moveon = True
                break
    
        
        testarray = [int( left )]
        
        if left[::-1] != right:
            testarray.append( int( right ))

        for testvalue in testarray:
        
            prime = checked.get( testvalue )

            if prime is None:
                p = getfactors( int( testvalue ), testprime = True )
                checked[testvalue] = p
                prime = p

            if not prime:
                moveon = True
                break
         
        if moveon:
            break
            
            
    if moveon:
        continue
    
    counter += 1
    print( '----',n )
    res += n
    
    if counter == 11:
        break

print( res )
    
        
    
    

