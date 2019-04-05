"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the 
following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""
res = []
i = 1
prevtotal = 0
total = 0
while True:
    prevtotal = total
    s = str( i )
    total += len( s )
    if prevtotal < 10 < total:
        res.append( int( s[-total + 10 - 1] ))
    
    elif prevtotal < 10 ** 2 < total:
        res.append( int( s[-total + 10 ** 2 - 1] ))

    elif prevtotal < 10 ** 3 < total:
        res.append( int( s[-total + 10 ** 3 - 1] ))

    elif prevtotal < 10 ** 4 < total:
        res.append( int( s[-total + 10 ** 4 - 1] ))

    elif prevtotal < 10 ** 5 < total:
        res.append( int( s[-total + 10 ** 5 - 1] ))

    elif prevtotal < 10 ** 6 < total:
        res.append( int( s[-total + 10 ** 6 - 1] ))

    else:
        if total > 10 ** 6:
            break
        
    i += 1
