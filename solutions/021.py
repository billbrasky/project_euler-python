"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which 
divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each 
of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 
110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; 
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from solutions.functions import getfactors


m = 10000
a = [True]*( m )

res = 0
for i in range( 1, m ):
    
    usable = a[i]
    
    if usable:
        
        value = sum( getfactors( i )) - i
        
        if value < m and value != i:
            
            value2 = sum( getfactors( value )) - value
            
            if value2 == i:
                print( i, value )
                res += i + value
                
                a[i] = False
                a[value] = False
                

print( res )
    
