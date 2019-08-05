# List is a collection which is ordered and changeable. Allows duplicate members.
# In Python lists are written with square brackets.
mylist = ["apple", "banana", "mango"]
print(mylist)

# Print the second item of the list:
print(mylist[1])

# Change the second item of the list:
mylist[1] = "orange"
print(mylist)

# Print all items in the list, one by one using for loop:

for x in mylist:
	print(x)	

#To determine if a specified item is present in a list use the in keyword
if "apple" in mylist:
	print("'apple' exists in list")

# Print the number of items in the list:
print(len(mylist))

#Using the append() method to append an item:
mylist.append("banana")
print(mylist)

# To add an item at the specified index, use the insert() method
mylist.insert(1, "peach")
print(mylist)

# The remove() method removes the specified item:
mylist.remove("orange")
print(mylist)

# The pop() method removes the specified index, (or the last item if index is not specified):
mylist = ["apple", "banana", "mango"]
mylist.pop()
print(mylist)

mylist = ["apple", "banana", "mango", "orange", "avocado"]
mylist.pop(3)
print(mylist)

# The del keyword removes the specified index:
mylist = ["apple", "banana", "mango", "orange", "avocado"]
del mylist[3]
print(mylist)

# The del keyword can also delete the list completely:
mylist = ["apple", "banana", "mango", "orange", "avocado"]
del mylist
# print(mylist)

# The clear() method empties the list:
mylist = ["apple", "banana", "mango", "orange", "avocado"]
mylist.clear()
print(mylist)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy

# Make a copy of a list with the copy() method:
mylist = ["apple", "banana", "mango"]
newlist = mylist.copy()
print(newlist)

# Make a copy of a list with the list() method:
newlist = list(mylist)
print(newlist)

# Using the list() constructor to make a List:
newlist = list(("apple", "banana", "mango"))
print(newlist)