# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a class named MyClass, with a property named x:
class MyClass:
	x = 5
	
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = Person("John", 13)
print(p1.name,"is",p1.age,"years old")

# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def echofunc(self):
		print(self.name,"is", self.age,"years old. From function.")
		
p1 = Person("John", 13)
p1.echofunc()

# You can modify properties on objects like this:
p1.age = 41
print(p1.name,"-",p1.age)

# Delete the age property from the p1 object:
del p1.age

# You can delete objects by using the del keyword:
del p1