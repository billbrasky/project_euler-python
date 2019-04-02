"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 
10 and base 2.

(Please note that the palindromic number, in either base, may not include leading 
zeros.)
"""

import re

def getcounts( n ):
    
    m = n
    counter = 0
    while True:
        m = m / 2
        
        if m > 1:
            counter += 1
        else:
            break

    return (counter, n - 2**counter)

def ten2two( n ):
    
    height, m = getcounts( n )
    res = [1] + [0]*( height )

    for i in range( height - 1, -1, -1 ):
    
        test = m - (2 ** i)
        if test >= 0:
            m = test
            res[-i-1] = 1
            
    return ''.join( [str( x ) for x in res] )


def test( s2, s10 ):
    
    if int( s2, 2 ) == s10:
        print( 'It works!' )

    else:
        print( 'It does not work!' )    


def ispalindrome( n ):
    
    s = str( n )
    
    if s != s[::-1]:
        return False
    
    return True
    

# must be odd
# which means leading digit must be odd
res = 0
for i in range( 1, 10**6, 2 ):
    
    if re.search( r'^[2468]', str( i )) is not None:
        continue

    if ispalindrome( i ):
        s2 = ten2two( i )

        if ispalindrome( s2 ):
            res += i
    
    
    
