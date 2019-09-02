from room import Room
from character import Enemy, Friend

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

# Set Dave's item to steal attribute
dave.set_item_to_steal("ring")

# Add Dave to dining hall
dining_hall.set_character(dave)

# Add new friendly character
catrina = Friend("Catrina","A friendly skeleton")

catrina.set_conversation("Why hello there.")

# Add Catrina to room
ballroom.set_character(catrina)

current_room = kitchen

dead = False

while dead == False:
	print( "\n" )
	current_room.get_details()
	
	inhabitant = current_room.get_character()
	
	if inhabitant is not None:
		inhabitant.describe()
	
	command = input("> ")
	
	if command in ["north", "east", "south", "west"]:
		# Move in given direction
		current_room = current_room.move(command)
	elif command == "talk":
		# Talk to the inhabitant
		inhabitant.talk()
		response = input("reply: ")
		print("You said: "+response)
	elif command == "fight":
		# Fight with the inhabitant
		print("What will you fight with?")
		fight_with = input("> ")
		if inhabitant.fight(fight_with) == True:
			# What happens if you win?
			print("You win!")
			msg = "Move to the next room."
			if current_room == kitchen:
				print("Move to dining hall [south]")
				command = input("> ")
			elif current_room == dining_hall:
				print("Move to kitchen [north] or ballroom [west]")
				command = input("> ")
			else:
				print("Move to dining room [east]")
				command = input("> ")
			current_room = current_room.move(command)
		else:
			# What happens if you loose?
			print("Better luck next time!")
			dead = True
	elif command == "steal":
		print("What will you steal?")
		item_steal = input("> ")
		if inhabitant.steal(item_steal) == True:
			msg = "Move to the next room."
			if current_room == kitchen:
				print("Move to dining hall [south]")
				command = input("> ")
			elif current_room == dining_hall:
				print("Move to kitchen [north] or ballroom [west]")
				command = input("> ")
			else:
				print("Move to dining room [east]")
				command = input("> ")
			current_room = current_room.move(command)
		else:
			# What happens if you loose?
			print("Better luck next time!")
			dead = True
	elif command == "sad":
		print("Do you want a hug? [yes/no]")
		ans = input("> ")
		if inhabitant.hug(ans) == True:
			print("Yay!")
		else:
			print("Better luck next time!")
			dead = True