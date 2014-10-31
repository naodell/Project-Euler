'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''

onesDict    = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'} 
teenDict    = {'10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
tensDict    = {'2':'twenty', '3':'thirty', '4':'forty', '5': 'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
powerDict   = {2:'hundred', 3:'thousand'}

count = 0
for i in range(1,1001):
    number = str(i)
    string = ''
    for j,k in enumerate(reversed(number)):
        if k == '0':
            continue

        if j > 1:
            if sum([int(digit) for digit in number[-j:]]) is 0:
                string = '{0} {1} '.format(onesDict[k], powerDict[j]) + string 
            else:
                string = '{0} {1} and '.format(onesDict[k], powerDict[j]) + string 
        elif j is 1 and k != '1':
            string = '{0} '.format(tensDict[k]) + string 
        elif j is 1 and k is '1':
            string = '{0} '.format(teenDict[number[-2:]]) + string 
        elif j is 0: 
            if i < 10:
                string = '{0} '.format(onesDict[number[-1:]]) + string 
            elif number[-2] != '1':
                string = '{0} '.format(onesDict[number[-1:]]) + string 
            else:
                continue

    count += len(string)-len(string.split())
    print '{0}\t{1}\t{2}'.format(i, string, len(string)-len(string.split()))

print 'And the answer is {0}'.format(count)
