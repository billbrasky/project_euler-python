"""
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

triplets = {}
res = (0, 0)
for m in range( 1, 1000 ):
    for n in range( 1, m ):
        
        
        a = m ** 2 - n ** 2
        s = a
        if s > 1000:
            break
        
        b = 2 * m * n
        s += b
        if s > 1000:
            break
        
        c = m ** 2 + n ** 2
        s += c
        if s > 1000:
            break
        #print( s )
        if triplets.get( s ) is None:
            triplets[s] = []
        
        d = 2
        multiple = s * d
        while multiple <= 1000:

            new = tuple( [x * d for x in [a, b, c]] )

            if triplets.get( multiple ) is None:
                triplets[multiple] = [new]
            
            else:
                if new not in triplets[multiple]:
                    triplets[multiple].append( new )
            
            d += 1
            multiple = s * d
            
        
        triplets[s] += [(a,b,c)]
        
        if len( triplets[s] ) > res[1]:
            res = (s, len( triplets[s] ))

data = list( triplets.items())
data = [(x[1], x[0]) for x in data]

print( res[0] )
