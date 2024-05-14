num1 = int(input("Enter first number : "))
opr = input("Enter the operator (+ , - , * , /) : ")
num2 = int(input("Enter second number : "))

match opr:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        if num2 == 0:
            print("Division not possible by 0")
        else:
            print(num1/num2)

    case _:
        print("Wrong operator !")


