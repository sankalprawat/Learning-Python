word = input("Enter a word to check the number of vowels it has :")

vowels = "aeiouAEIOU"
count = 0

for i in word:
    if i in vowels:
        count = count + 1

print("Number of vowels :", count)
