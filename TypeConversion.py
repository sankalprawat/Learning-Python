Integer_type = 29
Float_type = 31.5
addition = Integer_type + Float_type
print("Value: ", addition)
print("Type: ", type(addition))         # Implicit type


# Explicit Type

String_type = '29'
Int_type = 31

print("Data type before type casting: ", type(String_type))

String_type = int(String_type)

_add = Int_type + String_type

print("Value: ", _add)
print("Data type after type casting: ", type(String_type))

# Can also be done with float to string, int to string, float to string and vice - versa .
