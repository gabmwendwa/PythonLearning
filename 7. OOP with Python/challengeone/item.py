class Item():
	def __init__(self, name):
		self.name = name
		self.description = None
		self.items = {}
	
	def set_name(self, name):
		self.name = name
	
	def get_name(self):
		return self.name

	def set_description(self, description):
		self.description = description
	
	def get_description(self):
		return self.description
	
	def get_details(self):
		for building in self.items:
			shop = self.items[building]
			print( shop.get_name())
			print( "----------" )
			print( shop.get_description())
			print( "The "+shop.get_name()+" is "+building )
			print( "\n" )
	
	def link_item(self, item_to_link, building):
		self.items[building] = item_to_link
		# print( self.name + " linked rooms :" + repr(self.linked_rooms) )

	def move(self, building):
		if building in self.items:
			return self.items[building]
		else:
			print( "There is an error. Try again." )
			return self