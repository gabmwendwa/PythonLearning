from item import Item

phones = Item("Phones")
phones.set_description("This is a mall that sells phones only")

cars = Item("Cars")
cars.set_description("This is a car yard")

furniture = Item("Furniture")
furniture.set_description("This is plaza full of furniture")

phones.link_item(cars, "back")
cars.link_item(furniture, "front")
furniture.link_item(phones, "left")

current_item = phones

while True:
	print("\n")
	current_item.get_details()
	command = input("> ")
	current_item = current_item.move(command)
