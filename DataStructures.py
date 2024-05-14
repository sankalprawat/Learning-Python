# Lists(mutable, uses[]), Dictionary(mutable, uses{}) and Tuples(immutable, uses())

lists = [1, 2, 7, 4, 5, 6]
tuples = ("Hello", "Hi", "Hola", "Namaste")
dict = {"Name": "Sankalp", "Course": "BCA", "College": "Not Good !"}

lists[2] = 3            # Updation of a list
lists.append(7)         # Appending a list
del lists[6]            # deletion of list elements
print(lists)

dict["College"] = "Unfortunately JECRC !"    # Updating Dict
dict["Friends"] = "bunch of Broski's !!!"         # Appending the Dict

print("Name : ", dict["Name"])
print("College : ", dict["College"])
print("Friends :", dict["Friends"])


print(tuples)  # Cannot perform operations on tuples unfortunately as they are immutable !!!!!