# class Vehicle():
#     def __init__(self, bodystyle):
#         self.bodystyle = bodystyle
#
# class car(Vehicle):
#     def __init__(self, enginetype):
#         super().__init__("Car")
#         self.wheels = 4
#         self.doors = 4
#         self.engine = enginetype
#
# class Motorbike(Vehicle):
#     def __init__(self,hassidecar, enginetype):
#         super().__init__("Motorbike")
#         if(hassidecar):
#             self.wheels = 3
#         else:
#             self.wheels = 2
#         self.door = 0
#         self.enginetype = enginetype
#

try:
    number = input("Enter a number you want to divide by 10 : ")
    num = int(number)
    num = 10/num
except ZeroDivisionError as e:
    print("Cannot divide by zero")
except ValueError as e:
    print("Please enter a valid value")