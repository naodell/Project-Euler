'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''
import math

lop   = [2]
digits = ''.join([str(i) for i in range(1,10)])
for number in range(3,int(math.sqrt(10000000))):
    isPrime = True 
    for prime in lop:
        if prime > math.sqrt(number):
            break
        if number % prime == 0:
            isPrime = False
            break
    
    if isPrime:
        lop.append(number)

        isPandigi = False
        if sorted(str(number)) == digits:
            print number
            isPandigi = True
            
