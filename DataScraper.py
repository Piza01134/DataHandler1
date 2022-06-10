from openpyxl import load_workbook
from random import randrange
from datetime import datetime
from datetime import timedelta


#load spreadsheet
wb = load_workbook('Rain Spreadsheet.xlsx')

sYear = input("Starting Year (-1 for default): ")
if not sYear == "-1":
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

d1 = datetime.strptime(date1, '%Y/%m/%d')
d2 = datetime.strptime(date2, '%Y/%m/%d')

#generate random dates in range
def random_dates_generator(start, end, repeat: int, type: int):
    """
    This function will return a random datetime between two datetime 
    objects.
    
    type = -1: get rid of None values
    type = 0: get rid of 0 values and None values
    """

    dates = []
    k = 0
    while k < repeat:
        delta = end - start
        int_delta = (delta.days)
        random_day = randrange(int_delta)

        date = datetime.strftime(start + timedelta(days=random_day), '%Y/%m/%d')

        check = find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) )

        if type == -1:
            if not date in dates and not check == None:
                dates.append(date)
                k += 1   
        if type == 0:
            if not date in dates and not check == None and not check == 0:
                dates.append(date)
                k += 1 
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


type = int( input("(-1 to get rid of None) (0 to get rid of 0): ") )

while not type == -1 and not type == 0:
    type = int( input("(-1 to get rid of None) (0 to get rid of 0): ") )

dates = random_dates_generator(d1, d2, number, type)

for date in dates:
    print(date)
    print(date[0:4])
    print(int(date[5:7]))
    print(int(date[8:10]))
    print( find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) ) )


