'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

(see page for illustration)

How many routes are there through a 20x20 grid?
'''

gridSize = (2, 2)
numPaths = 0
numMoves = (0, 0)

while(numMoves[0] < gridSize[0] and numMoves[1] < gridSize[1]):
    numPaths = numPaths + 1

    if numMoves[0] == gridSize[0]: 
        
    if numMoves[1] == gridSize[1]:
