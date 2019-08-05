# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a: a + 10
print(x(5))

# A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b: a*b
print(x(5,20))

x = lambda a, b, c: a + b + c
print(x(6, 7, 8))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
	return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:
mydouble = myfunc(2)
print(mydouble(11))

# Or, use the same function definition to make a function that always triples the number you send in:
mytriple = myfunc(3)
print(mytriple(11))