def add(num1, num2):
    return num1 + num2  # Generic function with def keyword


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0 or num2 < 0:
        return "Error: Number cannot be zero or negative!"
    else:
        return num1 / num2


compare = lambda a, b: a if (a > b) else b  # lambda, inline or anonymous function

if __name__ == "__main__":
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print("The greater number is : ", compare(num1, num2))
    print("Sum : ", add(num1, num2))
    print("Sub : ", sub(num1, num2))
    print("Mul : ", mul(num1, num2))
    print("Div : ", div(num1, num2=0))
