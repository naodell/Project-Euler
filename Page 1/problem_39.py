''' 
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

import numpy as np

maxSol = 0
maxPer = 3
for perimeter in range(3,1000):
    #print perimeter, ':',
    nSol = 0
    for hypo in range(1, int(perimeter/2.)): 
        coeff = np.array([2, 2*(hypo - perimeter), (perimeter - hypo)**2 - hypo**2]) 
        sides = np.roots(coeff)

        if sides[0] == int(sides[0]) and sides[1] == int(sides[1]):
            nSol += 1

    if nSol > maxSol:
        maxSol, maxPer = nSol, perimeter

print 'The value of p that maximizes the solutions is {0} with {1} solutions'.format(maxPer, maxSol)
