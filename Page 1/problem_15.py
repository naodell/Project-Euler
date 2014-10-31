'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

(see page for illustration)

How many routes are there through a 20x20 grid?
'''

def element_counter(inList, target):
    count = 0
    for element in inList:
        if element == target:
            count += 1
    return count

gridSize    = 13
completePaths = []
partialPaths  = [[0], [1]]

# Generate paths
while (len(partialPaths) > 0):
    
    newPaths = partialPaths[:]
    partialPaths = []

    for i,path in enumerate(newPaths):
        rights  = element_counter(path, 0)
        downs   = element_counter(path, 1)

        if downs == gridSize and rights < gridSize:
            completePaths.append(path[:] + [0 for n in range(gridSize - rights)])
            continue

        if rights == gridSize and downs < gridSize:
            completePaths.append(path[:] + [1 for n in range(gridSize - downs)])
            continue

        if  rights < gridSize:
            partialPaths.append(path[:] + [0])

        if  downs < gridSize:
            partialPaths.append(path[:] + [1])


print 'And the answer is... {0}'.format(len(completePaths))
