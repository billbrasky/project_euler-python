"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 
5 spiral is formed as follows:

21 22 23 24 25
20   7   8   9 10
19   6   1   2 11
18   5   4   3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in 
the same way?
"""

def run() -> int:
    m = 1001

    a = [x*2 for x in range( 1, m ) if  x*2 < m ]
    start = 2
    current = start
    res = 1
    for x in a:

        end = current + x*4 - 1
        wanted = [end - x*i for i in range( 4 )]
        res += sum( wanted )
        current = end + 1

    return res

if __name__ == "__main__":
    print( run())