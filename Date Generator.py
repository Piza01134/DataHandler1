from random import randrange
from datetime import datetime
from datetime import timedelta
from time import sleep

file = open("dates.txt","w")

sYear = input("Starting Year (-1 for default) (0 for read): ")
if not sYear == "-1" and not sYear == "0":
    sMonth = input("Starting Month: ")
    sDay = input("Starting Day: ")
    eYear = input("Ending Year: ")
    eMonth = input("Ending Month: ")
    eDay = input("Ending Day: ")
else:
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

file.write("Start: " + date1 + "\n")
file.write("End: " + date2 + "\n")
file.write("Number: " + str(number) + "\n" + "\n")

d1 = datetime.strptime(date1, '%Y/%m/%d')
d2 = datetime.strptime(date2, '%Y/%m/%d')

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

def random_date_adder(start, end, lst):
    delta = end - start
    int_delta = delta.days
    random_day = randrange(int_delta)
    if not datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d') in lst:
            lst.append(datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d'))       
    return sorted(lst)
    

def print_list(lst):
    for x in lst:
        print(x)

def print_all(lst):
    print("yeaaaarrrrrrrrrrrrrrrrrrrrrrrrr")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        first = string.index("/")
        second = string.index("/", first + 1)
        print(string[0:first])

    print("Monnthhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        first = string.index("/")
        second = string.index("/", first + 1)
        print(string[first + 1:second])

    print("Dayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        first = string.index("/")
        second = string.index("/", first + 1)
        print(string[second + 1:])

finalDates = random_dates_generator(d1, d2, number)

print_list(finalDates)

change = input("Do you have any dates you would like to change? (y/n): ")

multiple = "y"

if change == "y":
    while multiple == "y":
        date = input("Input Day (yyyy/m/d): ")
        
        while date not in finalDates:
            date = input("Not in list! Try again (yyyy/m/d) (-1 to cancel): ")
            if date == "-1":
                break;

        if not date == "-1":
            finalDates.remove(date)
            finalDates = random_date_adder(d1, d2, finalDates)
            print_list(finalDates)

        multiple = input("More dates? (y/n): ")

print_list(finalDates)

for x in finalDates:
    file.write(x + "\n")

    
file.close()
