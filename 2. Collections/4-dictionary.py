# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

mdic = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1969
}
print(mdic)

# Get the value of the "model" key:
print(mdic["model"])

# There is also a method called get() that will give you the same result:
print(mdic.get("model"))

# You can change the value of a specific item by referring to its key name:
mdic["year"] = 2019
print(mdic)

# Print all key names in the dictionary, one by one:
for x in mdic:
	print(x)

# Print all values in the dictionary, one by one:
for x in mdic:
	print(mdic[x])
	
# You can also use the values() function to return values of a dictionary:
for x in mdic.values():
	print(x)

# Loop through both keys and values, by using the items() function:
for x, y in mdic.items():
	print(x, y)
	
# To determine if a specified key is present in a dictionary use the in keyword:
if "model" in mdic:
	print("Yes, \"model\" exists")	
else:
	print("None exists")
	
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
print(len(mdic))

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mdic["color"] = "red"
print(mdic)

# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
mdic.pop("model")
print(mdic)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
mdic.popitem()
print(mdic)

# The del keyword removes the item with the specified key name:
mdic = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1969
}

del mdic["model"]
print(mdic)

# The del keyword can also delete the dictionary completely:
del mdic
#print(mdic)

# The clear() keyword empties the dictionary:
mdic = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1969
}
mdic.clear()
print(mdic)

# Make a copy of a dictionary with the copy() method:
mdic = {
	"brand" : "Ford",
	"model" : "Mustang",
	"year" : 1969
}
ndic = mdic.copy()
print(ndic)

# Another way to make a copy is to use the built-in method dict().
odic = dict(mdic)
print(odic)

# It is also possible to use the dict() constructor to make a new dictionary:
vdic = dict(Brand="Ford", Model="Mustang", Year=1969)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(vdic)
