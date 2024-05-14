num = int(input("Enter a number to check if it's prime or not: "))

if num == 1 or num == 2:
    print("It's a prime number")

for i in range(2, num):
    if num % i == 0:
        print("It's a prime.")
else:
    print("It's not a prime")