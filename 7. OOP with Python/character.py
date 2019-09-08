class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
		
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    def set_name(self, char_name):
        self.name = char_name

    def get_name(self):
        return self.name

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
	enemies_defeated = 0
	
	def __init__(self, char_name, char_description):
		
		super().__init__(char_name, char_description)
		self.weakness = None
		self.item_to_steal = None
		self.enemy_defeat_count = 0
	
	def fight(self, combat_item):
		if combat_item == self.weakness:
			print("You fend " + self.name + " off with the " + combat_item )
			Enemy.enemies_defeated += 1
			return True
		else:
			print(self.name + " crushes you, puny adventurer")
			return False
	
	# get and set methods for number of enemies defeated
	def set_enemies_defeated(self, enemy_count):
		self.enemy_defeat_count = enemy_count
		
	def get_enemies_defeated(self):
		return self.enemy_defeat_count

	def get_enemies_defeats(self):
		return Enemy.enemies_defeated
	
	def set_weakness(self, item_weakness):
		self.weakness = item_weakness
		
	def get_weakness(self):
		return self.weakness
				
	def set_item_to_steal(self, item_steal):
		self.item_to_steal = item_steal
		
	def get_item_to_steal(self):
		return self.item_to_steal

	def steal(self, item_steal):
		print("You steal from "+ self.name)
		# How will you decide what this character has to steal?
		if item_steal == self.item_to_steal:
			print("You have stolen "+ item_steal + " from " + self.name)
			return True
		else:
			print(self.name + " does not have "+ item_steal)
			return False

class Friend(Character):
	def __init__(self, char_name, char_description):
		
		super().__init__(char_name, char_description)
		self.feeling = None
	
	def hug(self, char_feel):
		if char_feel == "yes":
			print(self.name + " hugs you back!")
			return True
		else:
			print(self.name + " is now sad as well!")
			return False