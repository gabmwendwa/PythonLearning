from character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("I want your brains!")

# Trigger a conversation with Dave
dave.talk()

# Trigger fight with Dave
dave.fight("Knife")

jack = Character("Jack", "The Hero")

jack.describe()

# Add some conversation for Jack when he is talked to
jack.set_conversation("What's up, dude!")

# Trigger a conversation with Jack
jack.talk()

# Add some conversation for Jack when he is talked to
jack.set_conversation("No brains for you today!")

# Trigger a conversation with Jack
jack.talk()

# Trigger fight with Jack
jack.fight("Shotgun")