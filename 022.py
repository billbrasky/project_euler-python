"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

import string

alpha = string.ascii_uppercase

names = []
with open('resources/names.txt', 'r') as f:
    names = f.read().split('\",\"')
    
names[0] = names[0][1:]
names[-1] = names[-1][:-1]


names.sort()

res = 0
for name in names:
    num_name = [alpha.index(letter)+1 for letter in name]
    name_sum = sum(num_name)*(names.index(name)+1)
    res += name_sum
    
print res