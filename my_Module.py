def sub(num1, num2):
    return float(num1) - float(num2)


def add(num1, num2):
    return float(num1) + float(num2)


def mul(num1, num2):
    return float(num1) * float(num2)


def div(num1, num2):
    if float(num2) == 0:
        print("Division not possible by 0")
    else:
        float(num1) / float(num2)


def greeting(name):
    print("Hello, how was your day", name)