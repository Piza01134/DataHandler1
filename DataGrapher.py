import matplotlib.pyplot as plt
from openpyxl import load_workbook
from scipy import stats

#pipenv shell

file = open("dates.txt", "r")

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


#create normal probablity plot
def npp(x, y):
    if not len(x) == len(y):
        return None
        
    show_graph(x, y, "Dates", "Precipitation in mm", "Precipitation vs. Time")

#display graph
def show_graph(x, y, x_label, y_label, title):
    # plotting the points 
    plt.scatter(x, y)

    # naming the x axis
    plt.xlabel(x_label)
    # naming the y axis
    plt.ylabel(y_label)
    
    # giving a title to my graph
    plt.title(title)
    
    # function to show the plot
    plt.show()

#load spreadsheet
wb = load_workbook('Rain Spreadsheet.xlsx')

text = file.read()

date = []
dates = text.split("\n")

rain = []
for date in dates:
    rain.append( find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) ) )

# x axis values
x = dates
# corresponding y axis values
y = rain

z_scores = stats.zscore(y)


# plotting the points 
plt.scatter(x, y)
  
# naming the x axis
plt.xlabel('Dates')
# naming the y axis
plt.ylabel('Precipitation in mm')
  
# giving a title to my graph
plt.title('Precipitation vs. Time')
  
# function to show the plot
plt.show()

file.close