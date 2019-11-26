"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and 
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import permutations

base = [str( x ) for x in range( 1, 10 )]

iterator = permutations( base )
res = 0

#s = '192384576'

tests = [
    (3, 3, 3),
    (2, 2, 2, 3),
    (1, 2, 2, 2, 2),
    (4, 5)
]

for thing in iterator: #[[str(x) for x in '192384576']]:
    s = ''.join( thing )
    si = int( s )

    if si < res:
        continue
    semires = 0
    for test in tests:
        
        x = [int( s[sum( test[:i] ):sum( test[:i] ) + test[i]] ) 
                for i in range( len( test ))]
                
        failed = False
        for i in range( len( x ) - 1 ):
            
            if x[0] * ( i + 2 ) != x[i + 1]:
                
                failed = True
                break
         
                
        if not failed:
            if si > semires:
                semires = si
        
    if semires != 0:
        print( semires, res)
        res = semires

print( res )
