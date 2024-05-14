months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
          8: "August", 9: "september", 10: "October", 11: "November", 12: "December"}

monthNum = int(input("Enter the month number to find the month: "))

for i in months:
    if i == monthNum:
        print(months[monthNum])