"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting sub-
string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note 
the following:

    d_2d_3d_4=406 is divisible by 2
    d_3d_4d_5=063 is divisible by 3
    d_4d_5d_6=635 is divisible by 5
    d_5d_6d_7=357 is divisible by 7
    d_6d_7d_8=572 is divisible by 11
    d_7d_8d_9=728 is divisible by 13
    d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


p = permutations( range( 10 ))


res = []
c = 0
for x in p:
    c +=1
    if ( x[0] == 0 or 
        x[3] % 2 != 0 or 
        sum( x[2:5] ) % 3 != 0 or
        x[5] % 5 != 0 ):
        continue
    
    
    sev = int( ''.join( [str( l ) for l in x[4:7]] ))
    ele = int( ''.join( [str( l ) for l in x[5:8]] ))
    thi = int( ''.join( [str( l ) for l in x[6:9]] ))
    svt = int( ''.join( [str( l ) for l in x[7:10]] ))
 
    
    if ( sev % 7 != 0 or
        ele % 11 != 0 or
        thi % 13 != 0 or
        svt % 17 != 0 ):
            continue
            
    res += [int( ''.join( [str( l ) for l in x] ))]
#print( res )
