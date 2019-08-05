# In Python a function is defined using the def keyword:
def myfunction():
	print("Hello from function")
# Call function	
myfunction()
print("-------")

# Information can be passed to functions as parameter.
def namefunc(fname):
	print(fname + " Mutisya")
namefunc("Mutua")
namefunc("Kalui")
namefunc("Mwendwa")
print("-------")

# The following example shows how to use a default parameter value.
# If we call the function without parameter, it uses the default value:
def mycountry(country = "Kenya"):
	print("I am from " + country)
mycountry("Tanzania")
mycountry("Rwanda")
mycountry()
mycountry("Uganda")
print("-------")

#You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as a parameter, it will still be a List when it reaches the function:
def myfunc(food):
	for x in food:
		print(x)

fruits = ["apple", "mango", "cherry"]
myfunc(fruits)
print("-------")

# To let a function return a value, use the return statement:
def myfunc(x):
	return 5 * x
print(myfunc(3))
print(myfunc(4))
print(myfunc(5))
print("-------")

# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
def tri_recursion(k):
	if(k>0):
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecursion Example Results")
tri_recursion(6)