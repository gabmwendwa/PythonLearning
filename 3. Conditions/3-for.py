# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# Loop through the letters in the word "banana":
for x in "banana":
	print(x)

# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana": break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": break
  print(x)
  
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": continue
  print(x)

print("----------")
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
	print(x)

print("----------")
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
	print(x)

print("----------")
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
	print(x)

print("----------")
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(5):
	print(x)
else:
	print("End of \"for\" loop")

print("----------")
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
	for y in fruits:
		print(x, y)
