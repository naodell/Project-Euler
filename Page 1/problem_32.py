'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

import math

pandigits = []
for multiplicand in range(1,2000):
    exponent = int(math.log(multiplicand, 10))

    for multiplier in range(min(multiplicand, pow(10, 9 - exponent))):
        product = multiplier*multiplicand
        digits = str(product) + str(multiplier) + str(multiplicand)
        if sorted(digits) == [str(i) for i in range(1,10)]:
            pandigits.append((multiplicand, multiplier, product))
            print (multiplicand, multiplier, product)

products = set([pantuple[2] for pantuple in pandigits])
print 'Sum of products of pandigitals is {0}'.format(sum(products))
