from room import Room

kitchen = Room()

kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

"""
print(kitchen.get_name())
print(kitchen.get_description())
kitchen.describe()
"""
dining_hall = Room()

dining_hall.set_name("Dining Hall")
dining_hall.set_description("A large room with tables and chairs.")

ballroom = Room()

ballroom.set_name("Ballroom")
ballroom.set_description("A vast room with shiny artifacts.")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

"""
kitchen.get_details()
dining_hall.get_details()
ballroom.get_details()
"""
current_room = kitchen

while True:
	print( "\n" )
	current_room.get_details()
	command = input("> ")
	current_room = current_room.move(command)
	