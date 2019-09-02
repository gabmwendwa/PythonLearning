from room import Room
from character import Enemy

kitchen = Room("Kitchen")
# kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
# dining_hall.set_name("Dining Hall")
dining_hall.set_description("A large room with tables and chairs.")

ballroom = Room("Ballroom")
# ballroom.set_name("Ballroom")
ballroom.set_description("A vast room with shiny artifacts.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")

# Add some conversation for Dave when he is talked to
dave.set_conversation("I want your brains!")

# Set Dave's weakness attribute
dave.set_weakness("water")

# Add Dave to dining hall
dining_hall.set_character(dave)

current_room = kitchen

while True:
	print( "\n" )
	current_room.get_details()
	
	inhabitant = current_room.get_character()
	
	if inhabitant is not None:
		inhabitant.describe()
	
	command = input("> ")
	current_room = current_room.move(command)
