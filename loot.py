from random import random, randint

def loot(inventory, level):
	luck=random()
	#items=""
	if level==1:
		if luck>.99:
			inventory[1]=1
			print "An Iron sword, how lucky!!"
			return inventory
		elif luck>.95:
			inventory[3]=1
			print "An, Iron Shield. That's quite rare."
			return inventory
		elif luck >.6:
			luck2=randint(1,3)
			if luck2==1:
				inventory[4]+=2
				print "Two potions. That's pretty good."
				return inventory
			elif luck2==2:
				inventory[4]+=1
				inventory[5]+=1
				print "A potion and A magic scroll. Nice!"
				return inventory
			elif luck2==3:
				inventory[5]+=2
				print "Two magic scrolls. How exciting!"
				return inventory
		elif luck>.4:
			inventory[5]+=1
			print "A magic scroll."
			return inventory
		elif luck>.05:
			inventory[4]+=1
			print "A potion."
			return inventory
		else:
			print "How unlucky, you didn't get anything."
			return inventory

			
