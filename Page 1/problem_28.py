'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''

spiralSize  = 1001 
spiral      = [[0 for i in range(spiralSize)] for j in range(spiralSize)]
direction   = 'left'
coordinate  = [0,spiralSize-1]

for number in reversed(range(1,pow(spiralSize,2)+1)):

    if direction == 'left':
        spiral[coordinate[0]][coordinate[1]] = number

        if coordinate[1] == 0:
            direction = 'down'
            coordinate[0] += 1
        elif spiral[coordinate[0]][coordinate[1]-1] != 0:
            direction = 'down'
            coordinate[0] += 1
        else:
            coordinate[1] -= 1

    elif direction == 'down':
        spiral[coordinate[0]][coordinate[1]] = number

        if coordinate[0] == spiralSize-1:
            direction = 'right'
            coordinate[1] += 1
        elif spiral[coordinate[0]+1][coordinate[1]] != 0:
            direction = 'right'
            coordinate[1] += 1
        else:
            coordinate[0] += 1

    elif direction == 'right':
        spiral[coordinate[0]][coordinate[1]] = number
        if coordinate[1] == spiralSize-1:
            direction = 'up'
            coordinate[0] -= 1
        elif spiral[coordinate[0]][coordinate[1]+1] != 0:
            direction = 'up'
            coordinate[0] -= 1
        else:
            coordinate[1] += 1

    elif direction == 'up':
        spiral[coordinate[0]][coordinate[1]] = number
        if coordinate[0] == 0:
            direction = 'left'
            coordinate[1] -= 1
        elif spiral[coordinate[0]-1][coordinate[1]] != 0:
            direction = 'left'
            coordinate[1] -= 1
        else:
            coordinate[0] -= 1


diagSum = 0
for i,row in enumerate(spiral):
    for j,entry in enumerate(row):
        if i + j == spiralSize - 1 or i == j:
            diagSum += entry

    #    print entry, '\t',
    #print ''

print 'And the answer is... {0}'.format(diagSum)
