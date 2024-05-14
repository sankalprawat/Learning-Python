import os

f = open("MyTxt.txt", 'a')
f.write("This some additional content !")
f = open("MyTxt.txt", 'r')
print(f.read())

f = open("MyTxt.txt", 'w')
f.write("Oops i accidentally deleted everything !!")

f = open("MyTxt.txt", 'r')
print(f.read())

# os.remove("MyTxt.txt")
