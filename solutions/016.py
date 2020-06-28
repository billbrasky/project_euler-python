"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def run() -> int:
    m = str( 2**1000 )

    res = 0

    for char in m:
        res += int( char )
        
    return res

if __name__ == "__main__":
    print( run())
