arr = [12, 52, 13, 42, 81, 92, 10]

find_num = int(input("Enter the number you want find in the List: "))

for i in range(len(arr)):
    if find_num == arr[i]:
        print("The given number is at index ", i)
        break
else:
    print("The provided number is not present in the List.")

