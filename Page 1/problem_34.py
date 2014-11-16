'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math

number = 11
answer = 0
while(number <  2.6e6):
    digits = str(number)
    digitSum = 0
    for digit in digits:
        digitSum += math.factorial(int(digit))

    if number == digitSum:
        answer += number

    number += 1 

print answer
