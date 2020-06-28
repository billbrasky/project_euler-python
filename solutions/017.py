""" 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-
two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""


data = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve'
]


def zeroto99( i: int, data: list ) -> str:

    prefix = {
        2: 'twen',
        3: 'thir',
        4: 'for',
        5: 'fif',
        6: 'six',
        7: 'seven',
        8: 'eigh',
        9: 'nine'
    }
    teen = 'teen'

    res = ''
    n = i%100
    
    if n <= 12:
        
        res += data[n]
        
    elif 12 < n <= 19:
        
        res += prefix[n%10] + teen
        
        if n == 14:
            res += 'u'
        
    elif 19 < n <= 99:
        
        res += prefix[n//10] + 'ty' + data[n%10]

    return res

def run() -> int:
    hundy = 'hundred'
    thou = 'thousand'
    andy = 'and'
    res = 0


    for i in range( 1, 1000 ):
        
        if i <= 99:
            word = zeroto99( i, data )
            
        elif 99 < i <= 999:
            
            word = data[i//100] + hundy
            
            if i % 100 != 0:
                word += andy
            
            word += zeroto99( i, data )
            
        #print( word )
        res += len( word )

    res += len( data[1] + thou )
        
    return res

if __name__ == "__main__":
    print( run())
