"""
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from solutions.functions import getfactors


def run() -> int:
    m = 999999

    while True:
        
        s = str( m )
        
        if s[0] != s[-1] or s[1] != s[-2] or s[2] != s[-3]:
            m -= 1
            continue
            
        a = getfactors( m )

        factor1 = max( a )
        factor2 = factor1 * min( a )
        
        if 100 < factor1 < 1000:
            
            otherfactor = m/factor1
        
            if 100 < otherfactor < 1000:
                
                res = m
                break

        if 100 < factor2 < 1000:
            
            otherfactor = m/factor2
            
            if 100 < otherfactor < 1000:
                
                res = m
                break

        m -= 1

    return res

if __name__ == '__main__':
    print( run())
