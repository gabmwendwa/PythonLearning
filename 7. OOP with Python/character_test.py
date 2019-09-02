from character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("I want your brains!")

# Trigger a conversation with Dave
dave.talk()

dave.set_weakness("water")

print("What will you fight with?")

fight_with = input()

dave.fight(fight_with)
