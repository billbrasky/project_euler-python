""" 
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find 
the value of the denominator.
"""


res = []

for x in range( 11, 100 ):
    
    if x % 10 == 0:
        continue
    
    sx = str( x )
    
    for y in range( x+1, 100 ):
        
        if y % 10 == 0:
            continue
    
        sy = str( y )
        
        if sy == sx[::-1]:
            continue
        
        sxy = sx + sy
        
        todrop = None
        for char in sxy:
            if sxy.count( char ) > 1:
                todrop = char
                break
                
        if todrop is None:
            continue
            
        ratio = x/y
        funnyratio = int( sx.replace( todrop, '', 1 )) / int( sy.replace( todrop, '', 1 ))

        if ratio == funnyratio:
            res.append( (x,y) )

        
        
