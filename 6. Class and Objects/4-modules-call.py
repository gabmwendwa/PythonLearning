# Now we can use the module we just created, by using the import statement:
import mymoduledefinition

mymoduledefinition.greeting("Gabriel Mwendwa")

print(mymoduledefinition.person1)
for x,y in mymoduledefinition.person1.items():
    print(x,y)

# You can create an alias when you import a module, by using the as keyword:
import mymoduledefinition as md
md.greeting("Mwendwa Mutisya")
print("---------------")

# There are several built-in modules in Python, which you can import whenever you like.
# Import and use the platform module:
import platform
x = platform.system()
print(x)
print("---------------")

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)
print("---------------")

# You can choose to import only parts from a module, by using the from keyword.
# The module named mymoduledefinition has one function and one dictionary:
# Import only the person1 dictionary from the module:
from mymoduledefinition import person1 as p1
for x,y in p1.items():
    print(x,y)
print("---------------")
