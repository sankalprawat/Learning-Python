list1 = [21, 52, 69, 81, 90]
number = int(input("Enter a number :"))
for i in range(len(list1)):
    if number == list1[i]:
        print("Given number is of index :", i)
        break
else:
    print("The number is not given in list.")


