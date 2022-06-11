from random import randrange
from datetime import datetime
from datetime import timedelta
from time import sleep

#default
sYear = "1990"
sMonth = "1"
sDay = "1"
eYear = "2020"
eMonth = "12"
eDay = "31"
    
number = int(input("Number of dates: "))

date1 = sYear + "/" + sMonth + "/" + sDay
date2 = eYear + "/" + eMonth + "/" + eDay

d1 = datetime.strptime(date1, '%Y/%m/%d')
d2 = datetime.strptime(date2, '%Y/%m/%d')

raw_date = datetime(2000, 5, 5)

year = raw_date.year
s = datetime(year, 3, 1)
e = datetime(year, 5, 31)
if s <= raw_date <= e:
    print("passed")


"""if type == 2: #get rid of 0 and only take Spring
year = raw_date.year
s = datetime(year, 3, 1)
e = datetime(year, 5, 31)
if not check == 0 and s <= raw_date <= e:
dates.append(date)
k += 1"""



def random_dates_generator(start, end, repeat):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    dates = []
    k = 0
    while k < repeat:
        delta = end - start
        int_delta = (delta.days)
        random_day = randrange(int_delta)
        if not datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d') in dates:
            dates.append(datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d'))
            k += 1         
    return sorted(dates)