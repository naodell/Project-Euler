'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

digits = ''
number = 1
while(len(digits) < 1000001):
    digits += str(number) 
    number += 1

print digits[1], digits[10], digits[100], digits[1000], digits[10000], digits[100000], digits[1000000],
print int(digits[0])*int(digits[9])*int(digits[99])*int(digits[999])*int(digits[9999])*int(digits[99999])*int(digits[999999])
