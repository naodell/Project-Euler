'''
Euler discovered the remarkable quadratic formula:

f(n) = n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, -79 and
1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.  

'''

from math import *

def function(number, a, b):
    return abs(pow(number,2) + a*number + b)

def is_prime(number):
    if number is 2:
        return True

    isPrime = True
    for factor in range(2,int(ceil(sqrt(number)))+1):
        if number%factor == 0:
            isPrime = False
            break
    return isPrime

maxPrime = 0
coefficients = [1,1]
for a in range(-1000,1000):
    for b in range(-1000,1000):
        number = 1
        while(is_prime(function(number,a,b))):
            number += 1

        if number > maxPrime:
            maxPrime = number
            coefficients = [a, b] 

print 'And the answer is... {0}'.format(coefficients[0]*coefficients[1])
