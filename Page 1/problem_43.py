'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

d_2 d_3 d_4 = 406 is divisible by 2
d_3 d_4 d_5 = 063 is divisible by 3
d_4 d_5 d_6 = 635 is divisible by 5
d_5 d_6 d_7 = 357 is divisible by 7
d_6 d_7 d_8 = 572 is divisible by 11
d_7 d_8 d_9 = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

def generate_permutations(elements):
    permutations = [[element] for element in elements]
    while len(permutations[0]) < len(elements):
        newPermutations = []
        for segment in permutations:
            for element in elements:
                if element not in segment: 
                    newSegment = segment[:]
                    newSegment.append(element)
                    newPermutations.append(newSegment)

        permutations = newPermutations

    return permutations

digits    = ''.join([str(i) for i in range(10)])
pandigits = generate_permutations(digits)
primes    = [2,3,5,7,11,13,17]

specialSum = 0
for pandigit in pandigits:
    isSpecial = True
    #print pandigit
    for i,prime in enumerate(primes):
        #print i+1,int(''.join(pandigit[i+1:i+4]))
        if int(''.join(pandigit[i+1:i+4]))%prime != 0: 
            isSpecial = False
            break

    if isSpecial:
        specialSum += int(''.join(pandigit))

print 'The sum of all 10-digit pandigitals with special properties is {0}'.format(specialSum)

