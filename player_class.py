#This is the player object
class Player(object):
	#Here we'll initialie the player's invetory and stat's.
	def __init__(self, inventory, stats):
		#The inventory order is, as of now: Wooden sword, Iron sword, wooden shield
		#Iron Shield, Potion, and magic scroll.
		
		self.inventory=inventory
		
		#Next's We're going to initiatlize both the move counter and the your base stats/vitals. Your base stats are,
		#in order: Hp and base damage. 
		
		self.stats = stats