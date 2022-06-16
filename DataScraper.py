from openpyxl import load_workbook
from random import randrange
from datetime import datetime
from datetime import timedelta

file = open("dates.txt", "w")

#load spreadsheet
wb = load_workbook('Rain Spreadsheet.xlsx')

sYear = input("Starting Year (-1 for default) (-2 for 1990) (-3 for 2020): ")
if sYear == "-1":
    #default
    sYear = "1990"
    sMonth = "1"
    sDay = "1"
    eYear = "2020"
    eMonth = "12"
    eDay = "31"
elif sYear == "-2":
    #default 1990
    sYear = "1990"
    sMonth = "1"
    sDay = "1"
    eYear = "1990"
    eMonth = "12"
    eDay = "31"
elif sYear == "-3":
    #default 2020
    sYear = "2020"
    sMonth = "1"
    sDay = "1"
    eYear = "2020"
    eMonth = "12"
    eDay = "31"
else:
    sMonth = input("Starting Month: ")
    sDay = input("Starting Day: ")
    eYear = input("Ending Year: ")
    eMonth = input("Ending Month: ")
    eDay = input("Ending Day: ")
    

number = int(input("Number of dates: "))

date1 = sYear + "/" + sMonth + "/" + sDay
date2 = eYear + "/" + eMonth + "/" + eDay

d1 = datetime.strptime(date1, '%Y/%m/%d')
d2 = datetime.strptime(date2, '%Y/%m/%d')


#generate random dates in range
def random_dates_generator(start, end, repeat: int, type: int):
    """
    This function will return a random datetime between two datetime 
    objects.
    """

    dates = []
    k = 0

    if not type == 5:
        while k < repeat:
            delta = end - start
            int_delta = (delta.days)
            random_day = randrange(int_delta)

            date = datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d')
            raw_date = datetime.strptime(date, '%Y/%m/%d')

            check = find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) )
            prop = 0

            #ensure no repeats and not None value
            if not date in dates and not check == None:
                if type == 0: #get rid of 0 values
                    if not check == 0:
                        dates.append(date)
                        k += 1 
                if type == 1: #get rid of 0 and only take Winter
                    month = raw_date.month
                    if not check == 0:
                        if month == 12 or month == 1 or month == 2:
                            dates.append(date)
                            k += 1
                if type == 2: #get rid of 0 and only take Spring
                    year = raw_date.year
                    s = datetime(year, 3, 1)
                    e = datetime(year, 5, 31)
                    if not check == 0 and s <= raw_date <= e:
                        dates.append(date)
                        k += 1
                if type == 3: #get rid of 0 and only take Summer
                    year = raw_date.year
                    s = datetime(year, 6, 1)
                    e = datetime(year, 8, 31)
                    if not check == 0 and s <= raw_date <= e:
                        dates.append(date)
                        k += 1
                if type == 4: #get rid of 0 and only take Fall
                    year = raw_date.year
                    s = datetime(year, 9, 1)
                    e = datetime(year, 11, 30)
                    if not check == 0 and s <= raw_date <= e:
                        dates.append(date)
                        k += 1
    elif type == 5: #give proportion of days that rained as well
        prop = 0
        while k < repeat:
            delta = end - start
            int_delta = (delta.days)
            random_day = randrange(int_delta)

            date = datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d')
            raw_date = datetime.strptime(date, '%Y/%m/%d')

            check = find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) )

            if not date in dates and not check == None:
                if check == 0:
                    prop += 1
                dates.append(date)
                k += 1
        print(prop / repeat)
    return sorted(dates)

#add random date to list
def random_date_adder(start, end, lst):
    delta = end - start
    int_delta = delta.days
    random_day = randrange(int_delta)
    if not datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d') in lst:
            lst.append(datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d'))       
    return sorted(lst)

#get value of total precipitation for date
#A=0; B=1; C=2;.....
def find_rain_data(year: str, month: int, day: int):
    #get reference to sheet
    ws = wb[ str(year) ]

    #find matching month
    for row in ws.rows:
        if row[6].value == month:
            row_index = row[6].row
            
            #loop through rows and find the matching date
            for row in ws.rows:
                if row[7].value == day and row[7].row >= row_index:
                    return row[23].value


type = int( input(""
                + "0 to get rid of 0" + "\n"
                + "1, 2, 3, 4 for winter, spring, summer, fall" + "\n"
                + "5 for proportion of days"
                + ": ") )

while not type in range(-1, 6):
    type = int( input(""
                + "0 to get rid of 0" + "\n"
                + "1, 2, 3, 4 for winter, spring, summer, fall" + "\n"
                + "5 for proportion of days"
                + ": ") )

dates = random_dates_generator(d1, d2, number, type)

for date in dates:
    file.write(date + "\n")

file.close()

