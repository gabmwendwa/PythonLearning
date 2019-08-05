# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thetuple = ("banana", "orange", "mango");
print(thetuple);

# You can access tuple items by referring to the index number, inside square brackets:
print(thetuple[1]);

# You can loop through the tuple items by using a for loop.
for x in thetuple:
	print(x);
	
# To determine if a specified item is present in a tuple use the in keyword:
if "apple" in thetuple:
	print("Yes, apple is present in tuple");
if "mango" in thetuple:
	print("Yes, mango is present in tuple");

# To determine how many items a tuple has, use the len() method:
print(len(thetuple));

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("banana", "orange", "mango")); # note the double rounded brackets
print(thistuple);