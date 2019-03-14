""" 
A unit fraction contains 1 in the numerator. The decimal representation of the 
unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen 
that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in 
its decimal fraction part.
"""

res = (0, 0)
mult = 1
for divisor in range( 2, 1000 ):
    
    seq = []
    zeros = 1
    repeat = True
    if 10 < divisor <= 100:
        mult = 2
        seq = [0]
    elif divisor > 100:
        mult = 3
        seq = [0,0]
        
    start = 10**mult
    dividend = 10**mult
    ds = []
    while True:
        if divisor == 901: print( dividend )
        if dividend in ds:
            ds
            break
        ds.append( dividend )
        test = dividend//divisor
        if test == 0:
            zeros += 1
            dividend = dividendfront*10**zeros
            continue
        
        seq.append( dividend//divisor )

        dividendfront = dividend - test * divisor
        dividend = dividendfront*10**zeros
        zeros = 1
#        print( dividend )
        if dividendfront*10*zeros == start:
            break


        if dividendfront == 0:
            repeat = False
            break
   
    print( ''.join([str(x) for x in seq]), divisor )
    if repeat:
        if len( seq ) > res[1]:
            res = (divisor, len( seq ))
            
print( res )
            
