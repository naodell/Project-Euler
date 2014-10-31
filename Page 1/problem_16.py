'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

'''

bigNumber = pow(2, 1000)
bigString = str(bigNumber)

powSum = 0
for number in bigString:
    powSum += int(number)

print bigNumber, powSum
