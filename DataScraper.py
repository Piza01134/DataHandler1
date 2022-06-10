from openpyxl import load_workbook
from random import randrange
from datetime import datetime
from datetime import timedelta

file = open('dates.txt', 'w')

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

file.write("Start: " + date1 + "\n")
file.write("End: " + date2 + "\n")
file.write("Number: " + str(number) + "\n" + "\n")

d1 = datetime.strptime(date1, '%Y/%m/%d')
d2 = datetime.strptime(date2, '%Y/%m/%d')

#generate random date
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


dates = random_dates_generator(d1, d2, number)
years = []
months = []
days = []

#split dates 
for date in dates:
    years.append( date[0:4] )
    months.append( date[5:7] )
    days.append( date[8:10] )

    #reference sheet
    ws = wb[ date[0:4] ]
    
    #loop through months and find the matching one
    for row in ws.iter_rows(1, None, 7, 7, False):
        for cell in row:
            if cell.value == date[5:7]:
                print(row)
                break

                    


