# Get the character at position 1 (remember that the first character has the position 0)
a = "Hello, World!"
print(a[1])

# Substring. Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(a[2:5])

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

# The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))

# The lower() method returns the string in lower case::
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case::
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # Return ['Hello', 'World!']

# Commant-line string input example
print("Please enter your name: ")
x = input()
print("Hello, ", x)
print("Hello, "+ x)
