'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

import math

lop     = [2]
answer  = 0
number  = 3
while(answer = 0):
    
    isPrime = True
    for prime in lop:
        if number%prime == 0:
            isPrime = False
            break

    if isPrime:
        lop.append(number)
    else:
        isGoldbach = False
        for prime in lop:
            multiplier = round(math.sqrt((number - prime)/2))
            if number == prime + 2*multiplier**2:
                isGoldbach = True
                break

        if isGoldbach == False:
            answer = number

    number += 1
