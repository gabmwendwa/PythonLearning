# Arrays are used to store multiple values in one single variable:
cars = ["Volvo", "Ford", "BMW"]
print(cars)

# Get value by index
print(cars[0])

# Modify array
cars[0] = "Toyota"
print(cars)

# Use the len() method to return the length of an array (the number of elements in an array).
print(len(cars))

# You can use the for in loop to loop through all the elements of an array.
for x in cars:
	print(x)
	
# You can use the append() method to add an element to an array.
cars.append("Honda")
cars2 = cars.copy()
print(cars)

# You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array:
cars.pop(1)
print(cars)

# Delete the element that has the value "Volvo":
cars.remove("Honda")
print(cars)
