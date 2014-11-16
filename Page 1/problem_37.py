'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import math

lop = [2]
nTP = 0
tpSum = 0
number = 3
while (nTP < 11):
#while (number < 1000):
    #find primes
    isPrime = True
    for prime in lop:
        if prime > math.sqrt(number):
            break
        if number % prime == 0:
            isPrime = False
            break
    
    if isPrime and number > 10:
        lop.append(number)

        #check if trunctable
        digits = str(number)
        length = len(digits)
        isTrunctable = True

        for i in range(int(length/2.)):
            if int(digits[i+1:]) not in lop:
                isTrunctable = False
                break
            if int(digits[:-(i+1)]) not in lop:
                isTrunctable = False
                break

        if isTrunctable:
            tpSum += number
            nTP += 1

    # end loop
    number += 1

print 'The sum of all eleven trunctable primes is {0}'.format(tpSum)
