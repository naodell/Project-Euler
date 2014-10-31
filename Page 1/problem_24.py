'''
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?  
'''

digits = [str(i) for i in range(10)]

segments        = [[digit] for digit in digits]
permutations    = []

for segment in segments:
    if len(segment) == len(digits):
        permutations.append(segment)
        continue

    for digit in digits:
        if digit not in segment:
            segments.append(segment[:] + [digit])

print 'And the answer is... {0}'.format(''.join(permutations[999999]))
