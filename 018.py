"""
Project Euler Problem 18
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
start
                                    75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
end
NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""

triList = []

#opens this file and reads the triangle of data into a list
with open('018.py', 'r') as f:
    grabInfo = False
    for line in f:
        if line.strip() == 'start':
            grabInfo = True
            continue
        if line.strip() == 'end':
            grabInfo = False
        if grabInfo == True:
            la = line.strip().split(' ')
            triList += [la]

pathSum = []

for row in triList:
    if len(row) == 1:
        pathSum += [[int(row[0]), 0]]
        continue

    tempSum = []
    for i in xrange(2**(triList.index(row)-1)):
        if i == 0:
            tempSum += [[ int(pathSum[i][0]) + int(row[i]), 0 ]]
            tempSum += [[ int(pathSum[i][0]) + int(row[i+1]), 1 ]]
        else:
            tempSum += [[ int(pathSum[i][0]) + int(row[(pathSum[i][1])]), pathSum[i][1]  ]]
            tempSum += [[ int(pathSum[i][0]) + int(row[(pathSum[i][1]+1)]), pathSum[i][1]+1 ]]
    pathSum = tempSum
#    print pathSum

t = [pathSum[i][0] for i in xrange(len(pathSum))]
print max(t)