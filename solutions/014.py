"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 
terms. Although it has not been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz( n: int ) -> int:
    
    if n%2 == 0:
        return n//2
        
    else:
        return 3 * n + 1
        

def run() -> str:
    collatzdic = {}

    i = 2
    res = (0,0)
    while i < 10**6:

        m = i
        
        counter = 1
        
        while m != 1:
        
            counter += 1

            m = collatz( m )
            if collatzdic.get( m ) is not None:
                
                counter += collatzdic[m]
                m = 1
        
        
        
        if counter > res[1]:
            res = (i, counter)
            
        collatzdic[i] = counter
        i += 1

    return str( res[0] )

if __name__ == "__main__":
    print( run())