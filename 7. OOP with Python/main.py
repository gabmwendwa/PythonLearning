from room import Room

kitchen = Room()

kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

print(kitchen.get_name())
print(kitchen.get_description())
kitchen.describe()