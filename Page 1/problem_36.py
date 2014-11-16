'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''
def is_palindrome(n):
    digits = str(n)
    length = len(digits)
    isPalindrome = True
    for i in range(int(length/2.)):
        if digits[i] != digits[-(i+1)]:
            isPalindrome = False
            break

    return isPalindrome

paliSum   = 0
bigNumber = 1000000
for n in range(bigNumber):
    binNum = bin(n)
    if is_palindrome(n) and is_palindrome(binNum[2:]):
        paliSum += n
        #print n, is_palindrome(n), binNum[2:], is_palindrome(binNum[2:]) 

print 'The sum of double-base palindromes below 1 million is {0}'.format(paliSum)
