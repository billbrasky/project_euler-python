"""
In England the currency is made up of pound, £, and pence, p, and there are eight 
coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from math import gcd
import time

start = time.time()

res = []
counter = 1
m = 201

for a in range( 0, m ):
    for b in range( 0, m, 2 ):
        if a % 2 == 0:
            if ( a + b ) % 10 != 0:
                continue
        else:
            if ( a + b ) % 5 != 0:
                continue
        
        if a + b > 200: break

        for c in range( 0, m, 5 ):
            if ( a + b + c ) % 10 != 0:
                continue
            if a + b + c > 200: break

            for d in range( 0, m, 10 ):
                if a + b + c + d > 200: break

                for e in range( 0, m, 20 ):
                    if a + b + c + d + e > 200: break

                    for f in range( 0, m, 50 ):
                        if a + b + c + d + e + f > 200: break

                        for g in range( 0, m, 100 ):
                            
                            s = a + b + c + d + e + f + g
                            
                            if s > 200:
                                break

                            if s == 200:
                                counter += 1
                                res.append( (a,b,c,d,e,f,g) )
final = {
    'res': res,
    'counter': counter,
    'time': time.time() - start
}                                

print( final['counter'] )
