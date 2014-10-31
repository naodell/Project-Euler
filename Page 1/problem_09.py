'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# a^2 + b^2 = (1000 - a - b)^2
# a^2 + b^2 = 1000^2 - 2000*(a + b) + (a + b)^2
# 0 = 1e6 - 2e3*(a + b) + 2*ab
# b = (2e3*a - 1e6) / (2*a - 2e3)

import sys,math,time

for a in range(1, 500):
    b   = (2000*a - 1000000) / (2*a - 2000)
    c2  = pow(a, 2) + pow(b, 2)
    c   = math.sqrt(c2)

    print 'a = {0}, b = {1}, c = {2}, abc = {3}'.format(a, b, c, a*b*c)
