"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


collatz_dic = {1: [1],
               2: [2, 1],
               3: [3, 10, 5, 16, 8, 4, 2, 1]}

n = 2
res = (n,2)
while n < 10000:
    m = n
    collatz_seq = [n]
    while m > 1:
        if m%2 == 0:
            m = m/2
        else:
            m = 3*m+1
        if m < len(collatz_dic.keys()):
            collatz_seq += collatz_dic[m]
            m = 1
        else:
            collatz_seq += [m]
    
    collatz_dic.update({n: collatz_seq})
    if len(collatz_seq) > res[1]:
        res = (n, len(collatz_seq))
    n += 1
        
print res[0]

    