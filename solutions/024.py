"""
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 
7, 8 and 9?
"""

from math import factorial

def run() -> str:
    m = 10**6

    start = [0]

    current = start

    step = 0
    notinuse = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        
        if len( current ) == 10:
            break
        
        combos = factorial( 10 - len( current ))
            
        if combos < m:
            
            notinuse.append( current[-1] )
            
            test = current[-1] + 1
            
            while test not in notinuse:
                
                test += 1
                if test == max( notinuse ):
                    break
                
                
            notinuse.remove( test )
            current[-1] = test
            
            m -= combos
            
        else:
            
            current.append( min( notinuse ))
            
    current = [str( x ) for x in current]

    return ''.join( current )

if __name__ == "__main__":
    print( run())
