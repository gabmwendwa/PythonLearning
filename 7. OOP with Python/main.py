from room import Room
from character import Enemy, Friend
from item import Item

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
dave.set_weakness("cheese")
dave.set_enemies_defeated(5)

# Set Dave's item to steal attribute
dave.set_item_to_steal("ring")

# Add Dave to dining hall
dining_hall.set_character(dave)

cheese = Item("cheese")
cheese.set_description("A large smelly block of cheese")
ballroom.set_item(cheese)

# Add new friendly character
catrina = Friend("Catrina","A friendly skeleton")

catrina.set_conversation("Why hello there.")

# Add Catrina to room
ballroom.set_character(catrina)

current_room = kitchen
backpack = []

dead = False

while dead == False:
	print( "\n" )
	current_room.get_details()
	
	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()
	
	item = current_room.get_item()
	if item is not None:
		item.describe()
	
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
		print("Defeat " + inhabitant.get_name() + " " + str(inhabitant.get_enemies_defeated() - inhabitant.get_enemies_defeats())+" times to win.")
		print("What will you fight with?")
		fight_with = input("> ")
		
		if fight_with in backpack:
			# fight enemy
			if inhabitant.fight(fight_with) == True:
				if inhabitant.get_enemies_defeats() < inhabitant.get_enemies_defeated():
					print("Good job! Keep on fighting to win!")
				else:				
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
		else:
			# Don't have item
			print("Sorry, you do not have "+fight_with+" in your backpack.")
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
		if inhabitant == None:
		  print("There is no one here to hug :(")
		else:
			if isinstance(inhabitant, Enemy):
				print("I wouldn't do that if I were you...")
			else:
				print("Do you want a hug? [yes/no]")
				ans = input("> ")
				if inhabitant.hug(ans) == True:
					print("Yay!")
				else:
					print("Better luck next time!")
					dead = True
	elif command == "take":
		if item is not None:
			backpack.append(item.get_name())
			current_room.set_item(None)
		else:
			print("Sorry! No items to collect in the "+current_room.get_name()+".")