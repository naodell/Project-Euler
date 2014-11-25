'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?  
'''

import math

lop     = [2]
answer  = 0
number  = 3
while(answer == 0):

    isPrime = True
    for prime in lop:
        if number%prime == 0:
            isPrime = False
            break

    if isPrime:
        lop.append(number)
    elif number%2 != 0:
        isGoldbach = False
        for prime in lop:
            multiplier = round(math.sqrt((number - prime)/2))
            if number == prime + 2*multiplier**2:
                isGoldbach = True
                break

        if isGoldbach == False:
            answer = number

    number += 1

print 'the smallest odd composite that cannot be written as the sum of a prime and twice a square is {0}'.format(answer)
