def factorial(num):
    if num == 0 or num == 1:
        return num
    else:
        return num * factorial(num-1)