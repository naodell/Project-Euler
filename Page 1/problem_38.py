'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192, 192 x 2 = 384, 192 x 3 = 576 

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

number = 1
panDigits = ''.join([str(i) for i in range(1,10)])
while(number < 100000):

    ccNumber     = 0
    multiplier   = 1
    ccString     = ''
    isPandigital = False
    while ccNumber < 1e10 and multiplier < number:
        ccString += str(number*multiplier)
        ccNumber = int(ccString)

        #print ccString, ''.join(sorted(ccString))
        if ''.join(sorted(ccString)) == panDigits:
            isPandigital = True
            break

        multiplier += 1


    if isPandigital:
        print number, ccNumber

    number += 1
