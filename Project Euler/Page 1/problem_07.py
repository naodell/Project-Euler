'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math, time

whichPrime  = 10001
lop         = [2]
count       = 3

while(len(lop) < whichPrime):
    isPrime = True 

    for n in lop:
        if n > math.sqrt(count):
            break

        if count % n == 0:
            isPrime = False
            break
    
    if isPrime:
        lop.append(count)

    count += 1

print lop[len(lop) - 1]
