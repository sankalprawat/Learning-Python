def is_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


num = int(input("Enter a number : "))
is_prime(num)