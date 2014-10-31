''' 
A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2     =   0.5
1/3     =   0.(3)
1/4     =   0.25
1/5     =   0.2
1/6     =   0.1(6)
1/7     =   0.(142857)
1/8     =   0.125
1/9     =   0.(1)
1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.  
'''

from decimal import *
getcontext().prec = 5000

maxPatternLen = [0,0]
for i in range(2,1000):
    number = str(Decimal(1)/Decimal(i))
    if len(number) < 50:
        continue

    pattern = ''
    for j,digit in enumerate(number[2:]):
        if len(pattern) is 0 and digit == '0':
            continue

        pattern = pattern + digit
        subPatterns = [pattern[k:] for k in range(len(pattern))]

        done = False
        for subPattern in subPatterns:
            if 2*subPattern == number[j+3:j+3+len(2*subPattern)]: 
                if len(subPattern) > 1:
                    pattern = subPattern
                    done = True
                    break

        if done == True:
            break

    if len(pattern) > maxPatternLen[1]:
        maxPatternLen = [i, len(pattern)]

print 'And the answer is... {0}\n'.format(maxPatternLen[0])
