'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''
import math

def generate_permutations(elements):
    permutations = [[element] for element in elements]
    while len(permutations[0]) < len(elements):
        newPermutations = []
        for segment in permutations:
            for element in elements:
                if element not in segment: 
                    newSegment = segment[:]
                    newSegment.append(element)
                    newPermutations.append(newSegment)

        permutations = newPermutations

    return permutations

def generate_primes(upperBound):
    # Generates all primes up to some upperbound
    lop   = [2]
    for number in range(3,upperBound):
        isPrime = True 
        for prime in lop:
            if prime > math.sqrt(number):
                break
            if number % prime == 0:
                isPrime = False
                break
        
        if isPrime:
            lop.append(number)

    return lop

#Generate all primes less than sqrt(Billion)
lop = generate_primes(int(math.sqrt(1e10)))

#Check if pandigits are prime
maxPandigit = 0
for order in range(3,10):
    digits = ''.join([str(i) for i in range(1,order)])
    pandigits = generate_permutations(digits)

    #Find largest prime pandigit
    for pandigit in pandigits:
        number = int(''.join(pandigit))
        isPrime = True
        for prime in lop:
            if prime > math.sqrt(number):
                break
            if number % prime == 0:
                isPrime = False
                break

        if isPrime and number > maxPandigit:
            maxPandigit = number

print 'The largest prime, n-digit pandigital number is {0}'.format(maxPandigit)
