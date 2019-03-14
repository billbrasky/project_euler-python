"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [i for i in xrange(7)]

year_start = 1901
year_end = 2001
day_start = 1
month_start = 0

day = day_start
sunday_counter = 0
for year in xrange(year_start, year_end):
    if year % 100 == 0:
        if year % 4 == 0:
            mdays[2] = 29
    elif year % 4 == 0:
        mdays[2] = 29
    else:
        mdays[2] = 28

    for month in mdays:
        if month == 0:
            continue
        
        day = (day + (month-1) % 7) % 7
        if day == 0:
            sunday_counter += 1
            

print sunday_counter