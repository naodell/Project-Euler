import sys, os
from math import *

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

def factorize(number, factors, primes):
    if target in primes or factors[-1] >= sqrt(number):
        return True, number

    for n in range(max(factors[-1], 2), int(ceil(sqrt(number)))+1):
        if n > sqrt(number):
            return True, number

        isPrime = True
        if n not in primes:
            for prime in primes:
                if n%prime == 0:
                    isPrime = False
                    break

        if isPrime:
            if n not in primes:
                primes.append(n)
            if number%n == 0:
                factors.append(n)
                number /= n
                break

    return False, number

target  = 600851475143
primes  = []
factors = [1]
isFactorized = False

while not isFactorized:
    (isFactorized, target) =  factorize(target, factors, primes)
    #print '{}'.format(target)

factors.append(target)
print set(factors)
