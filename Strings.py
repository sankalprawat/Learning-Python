# Different ways to concatenate strings

str1 = "How's JECRC ?"
str2 = "Worst !"

str3 = print("%s %s" % (str1, str2))    # Method 1

str3 = str1 + str2     # Method 1
print(str3)

print(" ".join([str1,str2]))        # Method 3

print("{} {}".format(str1, str2))    # Method 4

print(str1 , str2)       # Method 5

str4 = f"I study in Jecrc and {str1} {str2}"     # Method 6
print(str4)








