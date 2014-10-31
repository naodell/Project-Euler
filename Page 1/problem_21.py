'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).  If d(a) = b and d(b) = a, where a != b, then a
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import *

def factors(number):
    factors = []
    maxFactor = int(floor(sqrt(number)))
    for n in range(1,maxFactor+1):
        if number%n == 0:
            factors.extend([n, number/n])

    return sorted(list(set(factors)))

amicables = []
for i in range(1,10000):
    if i in amicables or len(factors(i)) == 2:
        continue

    factorSum1 = sum(factors(i)[:-1])
    factorSum2 = sum(factors(factorSum1)[:-1])
    if factorSum2 == i and i != factorSum1:
        amicables.append(i)
        amicables.append(factorSum1)

print 'And the answer is ... {0}'.format(sum(amicables))
