# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Any class can be a parent class, so the syntax is the same as creating any other class:
class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	
	def printname(self):
		print(self.fname,self.lname)
		
x = Person("John", "Doe")
x.printname()

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:
# NOTE: Use the pass keyword when you do not want to add any other properties or methods to the class.
class StudentA(Person):
	pass
x = StudentA("Jane", "Doe")
x.printname()

# Add the __init__() function to the Student class:
class StudentB(Person):
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
		Person.__init__(self, fname, lname)
x = StudentB("Peter", "Doe")
x.printname()

# Add a property called graduationyear to the Student class:
class StudentC(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)
		self.graduationyear = 2019
	def printmsg(self):
		print(self.fname, self.lname, "is graduating in the year", self.graduationyear)
x = StudentC("Emily", "Doe")
x.printmsg()

class StudentD(Person):
	def __init__(self, fname, lname, syear):
		Person.__init__(self, fname, lname)
		self.syear = syear
	def welcome(self):
		print("Weclome", self.fname, self.lname, "Class of", self.syear)
x = StudentD("Gabriel", "Mutisya", 2018)
x.welcome()
