'''
The nth term of the sequence of triangle numbers is given by, t_n = 0.5*n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''
import numpy as np
import string

#Generate first 1000 triangle numbers
fileName = 'p042_words.txt'
wordFile = open(fileName, 'r')
wordList = wordFile.readline().split(',')

nTriWords = 0
triNumbers = [0.5*n*(n+1) for n in range(1000)]
letterScores = dict(zip(string.ascii_uppercase, range(1,27)))
for word in wordList:
    word = word.strip('"')
    wordValue = 0
    for letter in word:
        wordValue += letterScores[letter]

    if wordValue in triNumbers:
        nTriWords += 1 

print 'The number of triangle words in {0} is {1}'.format(fileName, nTriWords)
