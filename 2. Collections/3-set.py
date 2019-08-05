# Set is a collection which is unordered and unindexed. No duplicate members.
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
	print(x)
	
# Check if "banana" is present in the set:
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("mango");
print(thisset)

# Add multiple items to a set, using the update() method:
thisset.update(["orange", "peach", "grapes"])
print(thisset)

# Get the number of items in a set:
print(len(thisset))

# Remove "banana" by using the remove() method:
thisset.remove("banana")
print(thisset)

# Remove "peach" by using the discard() method:
thisset.discard("peach")
print(thisset)

#You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
thisset.pop()
print(thisset)

# The clear() method empties the set:
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
"""
if thisset:
	print(thisset)
else:
	print("set does not exist")
"""	
# It is also possible to use the set() constructor to make a set.
thisset = set(["apple", "banana", "cherry"])
print(thisset)