# num = int(input("Enter a number : "))
# num = str(num)
# sumOfNum = 0
#
# for i in num:
#       sumOfNum += int(i)
#
# print("The sum of digit of given number is : ", sumOfNum)
#
# # Program to print the sum between the digit of two number
#
# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
#
# total_sum = 0
#
# for i in range(start, end + 1):
#
#     current_sum = 0
#     for j in str(i):
#         current_sum += int(j)
#     total_sum += current_sum
#
# print(f"The sum of digits between {start} and {end} is: {total_sum}")
#

# print the sum of numbers between two numbers

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total_sum = 0

# Directly calculate the sum within the loop
for number in range(start, end + 1):
    total_sum += number

print(f"The sum of numbers between {start} and {end} is: {total_sum}")