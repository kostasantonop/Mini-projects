while True:
    year = input("Year:")
    if year == "q":
        break
    else:
        year = int(year)
    disekto = False
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        disekto = True
    if disekto:
        print("This is a leap year!")
    else:
        print("This is not a leap year!")
print("End of programm")