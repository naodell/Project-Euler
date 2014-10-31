'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385 

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025 

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

'''
import sys,math

SUM = SUM2 = 0

for i in range(101):
    SUM  += i
    SUM2 += pow(i,2)

print '{0} - {1} = {2}'.format(pow(SUM,2), SUM2, pow(SUM,2) - SUM2)
