arr = [2, 4, 10, 15, 21, 39, 50]
data = int(input("Enter the number you want to find the index of: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == data:
        print("The element", data, "is found at index", mid)
        break
    elif data < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if low > high:
    print("Value not present")

# myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# data = int(input("Enter the data you want to find: "))
#
# low = 0
# high = len(myList) - 1
#
# while low <= high:
#
#   mid = (low + high) // 2
#
#   if data == myList[mid]:
#     print("The data is found at index ", mid)
#     break
#   elif data < myList[mid]:
#     high = mid - 1
#
#   else:
#     low = mid + 1
#
# if data != myList[mid]:
#   print("Value not present in Array !")