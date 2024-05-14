def fact(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * fact(num - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    num1 = int(input("Enter the number you want the factorial of : "))
    print("Factorial : ", fact(num1))
    n = int(input("Enter the number you want the fibonacci series of : "))
    print("The fibonacci series of the given number is : ")
    for i in range(n):
        print(fibonacci(i), end=" ")