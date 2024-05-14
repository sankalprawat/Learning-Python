def binary_search(a, data):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == data:
            return mid
        elif data < a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def is_array_sorted_recursive(A):
    n = len(A)
    if n <= 1:
        return True
    if A[n - 1] < A[n - 2]:
        return False
    return is_array_sorted_recursive(A[:-1])

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

Arr = []
print("Enter the elements of Array:")
for _ in range(10):
    Arr.append(int(input()))

print("Enter the number you want to find in the Array:")
data = int(input())

if is_array_sorted_recursive(Arr):
    result = binary_search(Arr, data)
    if result != -1:
        print(f"The given number is at index {result} in the Array.")
    else:
        print("The given number is not present in the Array.")
else:
    print("The Array you have given is not sorted.")
    print("Sorting the Array now... Please wait! ...")
    bubble_sort(Arr)
    print("The Array has been successfully sorted.")
    result = binary_search(Arr, data)
    if result != -1:
        print(f"The given number is at index {result} in the sorted Array.")
    else:
        print("The given number is not present in the Array.")
