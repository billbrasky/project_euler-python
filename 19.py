"""
You are given the following information, but you may prefer to do some research 
for yourself.

-    1 Jan 1900 was a Monday.
-    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
-    A leap year occurs on any year evenly divisible by 4, but not on a century 
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 
Jan 1901 to 31 Dec 2000)?
"""
thirties = ( 3, 5, 8, 10 )
thirtyones = ( 0, 2, 4, 6, 7, 9, 11 )


year, month, date, day = (1900, 0, 1, 1)

counter = 0
while (year, month, date) != (2001, 0, 1):
    if day == 0 and date == 1 and year > 1900:
        #print( '--------')
        counter += 1
                   
    day = ( day + 1 )%7
    date += 1
    
    if month in thirties and date == 31:
        month = ( month + 1 )%12
        date = 1
        
    elif month in thirtyones and date == 32:
        
        if month == 11:
            year += 1
        
        month = ( month + 1 )%12
        date = 1
        
    elif month == 1: # month is february
    
        leap = False
        century = True if year%100 == 0 else False
    
    
        if ( century and year%400 == 0 ) or ( not century and year%4 == 0 ):
            leap = True

        if ( leap and date == 30 ) or ( not leap and date == 29 ):
            month = 2
            date = 1

print( counter )
