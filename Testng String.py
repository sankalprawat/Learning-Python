import re

str1 = "Sankalp"
print(str)
print(re.match(str1, "Hello my name is Sankalp"))

text = ("Please contact us at contact@jecrcu.edu.in for further information. You can also give feedback at "
        "feedback@tp.com")

emails = re.findall(r"[a-z0-9.\-+_@]+[a-z0-9.\-+_]+\.[a-z]+", text)
print(emails)
