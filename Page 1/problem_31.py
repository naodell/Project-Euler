'''
In England the currency is made up of pound, $, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
It is possible to make $2 in the following way:

1*$1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can $2 be made using any number of coins?
'''

#from numpy import *
import math

subdivisions = [1, 2, 5, 10, 20, 50, 100, 200]
multipliers = {1:0, 2:1}

for i,subdiv1 in enumerate(subdivisions[2:]):
    print '{0}: '.format(subdiv1),
    nCombos = 1
    for j,subdiv2 in enumerate(subdivisions[1:i+2]):
        multiplier = multipliers[subdiv2]
        nCombos += 1 + multiplier*math.floor(subdiv1/subdiv2 - 1)

        print '1 + {0}*({1}/{2} - 1) = {3}; '.format(multiplier, subdiv1, subdiv2, 1 + multiplier*math.floor(subdiv1/subdiv2 - 1)),

    multipliers[subdiv1] = int(nCombos)

    print ''

print multipliers

target = 200;
ways = (target+1)*[0]
ways[0] = 1
 
for i,subdiv1 in enumerate(subdivisions):
    print i, subdiv1
    for j in range(subdiv1,target+1):
        ways[j] += ways[j - subdiv1]

print dict(zip(range(target+1),ways)) 
