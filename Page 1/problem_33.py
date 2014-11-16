'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

magicNumbers = []
for denominator in range(10,100):
    for numerator in range(10,denominator):
        denomDigits = list(str(denominator)) 
        numerDigits = list(str(numerator)) 

        commonIndex = (-1,-1)
        for digit in denomDigits:
            if digit in numerDigits and digit != '0':
                commonIndex = (numerDigits.index(digit), denomDigits.index(digit))
                break

        if commonIndex[0] is not -1:
            del numerDigits[commonIndex[0]]
            del denomDigits[commonIndex[1]]

            newNumer = int(numerDigits[0])
            newDenom = int(denomDigits[0])
            if newDenom is not 0:
                if float(numerator)/float(denominator) == float(newNumer)/float(newDenom):
                    magicNumbers.append((numerator, denominator, newNumer, newDenom))

superNumer = 1
superDenom = 1
for number in magicNumbers:
    superNumer *= number[2]
    superDenom *= number[3]

print superNumer, superDenom


