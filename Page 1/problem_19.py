'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

dayMap  = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
weekDay = 1 
firstSundays = 0
for year in range(1901,2001):
    for month in range(12):
        if month in [0, 2, 4, 6, 7, 9, 11]:
            nDays = 31
        elif month in [3, 5, 8, 10]:
            nDays = 30
        else:
            if year%4 is 0:
                nDays = 29
            else:
                nDays = 28

        for day in range(nDays):
            weekDay += 1

            if weekDay%7 is 0:
                if day is 0:
                    firstSundays += 1
                weekDay = 0
                
print firstSundays
