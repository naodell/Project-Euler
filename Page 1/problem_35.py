'''
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
'''
import math

def int_rotator(n,order):
    if n < 10: 
        return n

    digits = str(n)
    newNumber = digits[order:] + digits[:order] 

    return int(newNumber)

# generate list of primes
lop = [2]
bigNumber = 1000000
for n in range(3,bigNumber):

    isPrime = True
    for prime in lop:
        if prime > math.sqrt(n):
            break
        if n % prime == 0:
            isPrime = False
            break
    
    if isPrime:
        lop.append(n)

print 'Found all primes less than {0}.  Now checking rotations...'.format(bigNumber)
    
nCP = 0
for prime in lop:
    isCircular  = True
    for i in range(1,len(str(prime))):
        rotNumber = int_rotator(prime, i)
        if rotNumber not in lop:
            isCircular = False
            break

    if isCircular: nCP += 1

print 'The number of circular primes less than {0} is {1}'.format(bigNumber, nCP)
