'''
Pentagonal numbers are generated by the formula, P_n=n(3n-1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference are pentagonal and D = |P_k - P_j| is minimised; what is the value
of D?
'''
import numpy as np

def is_pentagonal(n)
    coeff = np.array([1.5, -0.5, -1*n])
    roots = np.

pentNums = []
isOptimized = False
count = 1
while(not isOptimized):
    newPentNum = int(0.5*count*(3*count -1))

    for number in pentNums:
        pentSum  = newPentNum + number
        pentDiff = abs(newPentNum - number)
     
    pentNums.append(newPentNum)
    count += 1
    if count == 20: isOptimized = True
