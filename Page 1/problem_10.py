'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math, time

lop         = [2]
count       = 3

while(count < 2000000):
    isPrime = True 

    for n in lop:
        if n > math.sqrt(count):
            break

        if count % n == 0:
            isPrime = False
            break
    
    if isPrime:
        #print count
        #time.sleep(1)
        lop.append(count)

    count += 1

print sum(lop)
