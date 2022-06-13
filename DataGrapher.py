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


#create histogram
def hist(x, y):
    if not len(x) == len(y):
        return None
    
    plt.hist(y)
    show_graph("Amount", "Frequency", "Histogram")   

#create normal probablity plot
def npp(x, y):
    if not len(x) == len(y):
        return None
    
    x = sorted(x)
    y = sorted(y)

    num = len(x)

    temp = []
    z_scores = []

    for i in range(num):
        temp.append( (i - 0.375) / (y[i] + 0.25) )

    z_scores = stats.zscore(temp)

    plt.scatter(x, z_scores)
    show_graph("Dates", "Expected z-score", "Normal Probability Plot")

#display graph
def show_graph(x_label, y_label, title):

    # naming the x axis
    plt.xlabel(x_label)
    # naming the y axis
    plt.ylabel(y_label)
    
    # giving a title to my graph
    plt.title(title)
    
    # function to show the plot
    plt.show()

#switch between options
def graph_swtich(type, x, y):
    match type:
        case 0:
            return npp(x, y)
        case 1:
            return hist(x, y)


#load spreadsheet
wb = load_workbook('Rain Spreadsheet.xlsx')

text = file.read()

date = []
dates = text.split("\n")

rain_amount = []
for date in dates:
    rain_amount.append( find_rain_data( date[0:4], int(date[5:7]), int(date[8:10]) ) )

# x axis values
#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = dates

# corresponding y axis values
#y = [5, 5, 5, 5, 2000, 5, 5, 5, 26, 313, 20]
y = rain_amount

type = 1
while not type == -1:

    type = int( input(""
                + "-1 for cancel" + "\n"
                + "0 for Normal Probability Plot" + "\n"
                + "1 for Histogram" 
                + ": ") )


    while not type in range(-1, 2):
        type = int( input(""
                    + "-1 for cancel" + "\n"
                    + "0 for Normal Probability Plot" + "\n"
                    + "1 for Histogram" 
                    + ": ") )

    graph_swtich(type, x, y)

file.close