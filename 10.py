"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

array = [1]*2*10**6
res = 0

i = 2
while i < len( array ):
	pos = array[i]
	
	if pos == 1:
		res += i
		
		x = i + i
		while x < len( array ):
			array[x] = 0
			
			x += i
			 	
	i += 1
	
print( res )
