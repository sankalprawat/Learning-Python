# program to demonstrate different number data types :
int_type = input("Enter a integer type number : ")
float_type = input("Enter a float type number : ")
complex_type = input("Enter a complex type number : ")

int_type = int(int_type)
float_type = float(float_type)
complex_type = complex(complex_type)

print(f"{int_type} this is a ", type(int_type))
print(f"{float_type} this is a ", type(float_type))
print(f"{complex_type} this is a ", type(complex_type))

