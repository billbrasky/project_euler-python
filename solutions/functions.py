
import math 

def getfactors( n, primefactors = True, testprime = False, countonly = False ):

    m = n
    counter = 2

    if primefactors:
        res = []
    else:
        res = [1,n]
    
    for i in range( 2, math.floor( math.sqrt( n )) + 1 ):
#        print( i )

        if i == m:
            break
        
        value = i
        while m > i and m % i == 0:
            
            if countonly and False:
                counter += 1
                
                if value != n//value:
                    counter += 1
            else:
                
                if value in res:
                    break
                if getfactors( value, False, testprime = True):
                    res.append( value )
                
                if value != n//value:
                    if getfactors( n//value, False, testprime = True):
                        res.append( n//value )
                

            m = m//i
            value *= i
        m = n

        if testprime and len( res ) > 2:
            return False

#            firstpass = False

    if testprime:
        return True

    if countonly:
#        counter += counter
        
        return len( res )
    
    else:

        if not primefactors:
            newres = []
            for i in range( len( res )):
                for j in range( i+1, len( res )):
                
                    temp = res[i]*res[j]
                
                    if temp != n and temp not in newres:
                        newres.append( temp )
            res += newres
                
                
        return res
        #return( list( set( res )))
        

def getprimes( n ):
    
    l = [0, 0] + [1] * ( n - 1 )
    
    i = 2

    primes = []
    
    while i <= n:
        
        if l[i] == 1:
        
            primes.append( i )
            for j in range( i + i, n + 1, i ):
                
                l[j] = 0

        i += 1
                
    return primes
                    
