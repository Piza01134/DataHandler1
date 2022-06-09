file = open("dates.txt", "r")

text = file.read()

dates = text.split("\n")

header = dates[0] + dates[1] + dates[2] + dates[3]

dates.pop(0)
dates.pop(0)
dates.pop(0)
dates.pop(0)

file.close()

#sort
file = open("dates.txt", "w")

file.write(header)

dates.sort()

for x in dates:
    file.write(x)

file.close()
