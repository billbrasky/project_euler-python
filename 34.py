"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their 
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

fact = [factorial( x ) for x in range( 10 )]
res = 0

for i in range( 10, 3*10**6 ):
    
    s = str( i )
    l = len( s )
    moveon = False
    
    choices = {z: fact[z] for z in range( 10 ) if len(str( fact[z] )) <= l}
    testsum = 0
    for c in s:
        if choices.get( int( c )) is None or testsum > i:
            
            moveon = True
            break
        testsum += choices[int( c )]
        
    if moveon:
        continue

    if testsum == i:
        print( testsum )
        res += testsum
    
