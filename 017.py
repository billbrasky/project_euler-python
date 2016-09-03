"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

h = 'hundred'
t = 'thousand'
nd = {1: ['one', 'eleven', 'ten'],
      2: ['two', 'twelve', 'twenty'],
      3: ['three', 'thirteen', 'thirty'],
      4: ['four', 'fourteen', 'forty'],
      5: ['five', 'fifteen', 'fifty'],
      6: ['six', 'sixteen', 'sixty'],
      7: ['seven', 'seventeen', 'seventy'],
      8: ['eight', 'eighteen', 'eighty'],
      9: ['nine', 'nineteen', 'ninety'],
      }


'''
res = 0

n = 1
l = []
while n < 1000:
    if n < 10:
        r = nd[n][0]
    elif 10 < n < 20:
        r = nd[n%10][1]
    elif n < 100:
        if n % 10 == 0:
            r = nd[n/10][2]
        else:
            r = nd[(n-n%10)/10][2] + nd[n%10][0]
    else:
        if n%100 == 0:
            r = nd[n/100][0]+h
        else:
            hAnd = nd[(n-n%100)/100][0] + h + 'and'
            if n % 100 < 10:
                r = hAnd + nd[n%10][0]
            elif 10 < n % 100 < 20:
                r = hAnd + nd[n%10][1]
            elif n % 10 == 0:
                r = hAnd + nd[n%100/10][2]
            else:
                r = hAnd + nd[(n%100-n%10)/10][2] + nd[n%10][0]
    l.append(r)
    n += 1
for el in l:
    print el
print len(l)
'''

res = 0
h = 900*len('hundred') + 891*len('and')
t = len('onethousand')
for key in nd.keys():
    if key != 1:
        res += 100*len(nd[key][2])
    else:
        res += 10*len(nd[key][2])
    res += 190*len(nd[key][0])+10*len(nd[key][1])

res += h+t
print res