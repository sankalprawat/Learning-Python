num1 = input("Enter first number : ")
opr = input("Enter the operator (+ , - , * , /) : ")
num2 = input("Enter second number : ")

if opr == '+':
    print("The addition of given number is : ", int(num1) + int(num2))

elif opr == '-':
    print("The subtraction of given number is : ", int(num1) - int(num2))

elif opr == '*':
    print("The multiplication of given number is : ", int(num1) * int(num2))

elif opr == '/':
    print("The division of given number is : ", int(num1) / int(num2))

else:
    print("Enter the correct operator !!")

print("Thank you for using my calculator.")
