'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

solution    = 0
maxLen      = 0

for num in range(2,int(1e6)):
    
    n_i = num
    count = 1

    while(n_i != 1):

        if n_i%2 == 0:
            n_i = n_i/2
        else:
            n_i = 3*n_i + 1
        
        count = count + 1

    if count > maxLen:
        solution    = num
        maxLen      = count

print '\n Solution is {} with a sequence length of {} '.format(solution, maxLen)
