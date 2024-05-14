# It's a mixture of DCS and String Checker
upper_case = 0
lower_case = 0
digit_case = 0

_str = input("Enter a string : ")

for char in _str:
    if char.isupper():
        upper_case += 1

    elif char.islower():
        lower_case += 1

    elif char.isdigit():
        digit_case += 1


print(f"There are {upper_case} upper case, {lower_case} lower case and {digit_case} digits in the given string.")


# Now a program to print 0 - 20 using loops

for i in range(20, 0, -1):
    print(i)