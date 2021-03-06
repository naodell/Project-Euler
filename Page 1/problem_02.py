import sys,math

'''
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... (f_n+1 = f_n + f_n-1)

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.o
'''

fib_seq = []
fib_even = []
fib_seq.extend([1, 1])
i=2

while(fib_seq[i-1] < 4e6):
    fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    if fib_seq[i] in range(0, int(4e6), 2):
        fib_even.append(fib_seq[i])
    i += 1

print sum(fib_even) 
