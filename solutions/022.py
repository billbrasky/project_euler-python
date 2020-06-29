#! /usr/bin/python3
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string
import io
alphabet = ':' + string.ascii_uppercase


def getscore( s: str ) -> str:
    
    res = 0
    
    for letter in s:
        
        res += alphabet.index( letter )
        
    return res

def run() -> int:
    res = []
    with open( 'names.txt', 'r' ) as f:

        for line in f:
            line = line.strip()[1:-1]
            
            if res == [] or line > res[-1]:
                
                res.append( line )
                
            else:
                
                i = -2
                
                while True:
                    if line > res[i]:
                        res = res[:i+1] + [line] + res[i+1:]
                        break
                        
                    if res[0] == res[i]:
                        
                        res = [line] + res
                        break
                        
                    i -= 1
            
                    
        
    result = 0

    i = 0
    for i in range( len( res )):
        
        name = res[i]
        
        result += getscore( name ) * ( i + 1 )

    return result


if __name__ == "__main__":
    print( run())
    


