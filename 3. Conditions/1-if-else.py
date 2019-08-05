# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
a = 33
b = 200
c = 33
if a < b:
	print("b is greater than a")
else:
	print("a is greater than b")

if a > c:
	print("a is greater than c")
elif a == c:
	print("a is equal to c")

# If you have only one statement to execute, you can put it on the same line as the if statement.
if b > a: print("b is greater than a")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a > b else print("EQUAL") if a == b else print("B")

# The and keyword is a logical operator, and is used to combine conditional statements:
# AND logic
if b > a and a == c:
	print("Both conditions are True")
	
# OR logic
if b < a or a == c:
	print("At least one of the conditions is True")