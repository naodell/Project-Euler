import os, sys
from math import *

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


for n1 in reversed(range(900, 1000)):
    for n2 in reversed(range(n1, 1000)):
        candidate   = str(n1*n2)
        places      = len(candidate)
        palindrome  = True

        for i,digit in enumerate(candidate):

            if i > places/2.:
                break

            if candidate[i] != candidate[-(i+1)]:
                palindrome = False
                break

        if palindrome:
            print '{0} x {1} = {2}'.format(n1, n2, candidate)

