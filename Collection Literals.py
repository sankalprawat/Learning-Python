# List type
my_list = ["Sankalp", "Rawat", 29, 2005, "July"]
print(my_list)
print(my_list[0])
print(len(my_list))

my_list[1] = "Hello !"
print(my_list[1])   # List are mutable

my_tuple = ("Sankalp", "Rawat", 29, 2005, "July")   # Tuple Type

print(my_tuple)
# my_tuple[1] = "Hello !"  # It will throw a error as tuples are not mutable
print(my_tuple[1])

# Dictionary type

my_dict = {"Sankalp": 7073075214, "Mom": 9509731626, "Dad": 9928915190, }   # A simple phonebook

print(my_dict)

print(my_dict["Sankalp"])

# print(my_dict[9928915190]) It will throw an error as we can only find the value using key not key using value

