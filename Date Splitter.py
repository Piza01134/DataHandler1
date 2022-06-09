
def print_all(lst):
    print("yeaaaarrrrrrrrrrrrrrrrrrrrrrrrr")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        if "/" in x:
            first = string.index("/")
            second = string.index("/", first + 1)
        print(string[0:first])

    print("Monnthhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        if "/" in x:
            first = string.index("/")
            second = string.index("/", first + 1)
        print(string[first + 1:second])

    print("Dayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    for x in lst:
        if "/0" in x:
            string = x.replace("/0", "/")
        else: string = x
        if "/" in x:
            first = string.index("/")
            second = string.index("/", first + 1)
        print(string[second + 1:])

file = open("dates.txt", "r")

text = file.read()

dates = text.split("\n")

for x in dates:
    print(x)

dates.pop(0)
dates.pop(0)
dates.pop(0)
dates.pop(0)

print_all(dates)

file.close()
