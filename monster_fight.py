#This Module contains funtions for fighting monsters of differnt levels. All levels
#Require your inventory, and your stats.
from random import randint, random
from get_response import get_str_response
from sys import exit
from loot import loot

def monster_l1(inventory, stats):
	#Pulls your Statistics from stats
	hp=stats[0]
	base_damage=stats[1]
	
	#Here we prime the out put of our function being a dictionary. The fist key is out inventory, the second our stats,
	#The third, the type of monster, and the fourth the boolean false value. This is used for when we run. The parent
	#function will check this. If true, if will generate a random room to go to instead of the usual ones.
	output={"inventory":inventory,"stats":stats,"enemy":"","run":False}
	
	#Sets monster hp
	ehp=100.0
	
	#This next statement checks to see what weapon you have and sets your damage multiplier
	if inventory[1]==1:
		weapon_damage_multiplier=1.5
	else:
		weapon_damage_multiplier=1.0
		
	#This next statment checks to seet what shield you have sets the armor damage reduction
	
	if inventory[3]==1:
		armor_damage_reduction=.66
	else:
		armor_damage_reduction=1.0
	
	#Creating the dictionary for get_response
	combat_options={
	"Help":["\nYour options are 1: Attack","\t\t 2: Defend","\t\t 3: Run Away", "\t\t 4: Use Item"],
		"Valid_Inputs":["attack","defend","run","item"]
	}
	item_options={
	"Help":["\nYour options are 1: Use Potion","\t\t 2: Use Magic Scroll"],
		"Valid_Inputs":["potion","scroll","magic"]
	}
	item_prompt="Which item would you like to use? \n"
	#determines which monster you face
	enemy=randint(1,2)
	#enemy=2
	
	if enemy==1:
		monster="Pack of goblins"
		output["enemy"]=monster
		prompt="What's your next move against the %s?.\n" % monster
		print "You have a encountered %s. Time for battle!!\n" % monster
		
		#setting a counter. The allows the while loop to alernate between your move and the monters
		counter=0
		
		#These lines allow attacks to deal more or less damage. Defending/running away will changing these
		hero_damage_multiplier=1.0
		monster_damage_multiplier=1.0
		
		#Initializes the monsters moves
		enraged=False
		decision = 1
		
		
		#While loop in which the battle actually takes place
		while hp>0 and ehp>0:
			#If counter is Even, the hero moves
			if counter % 2==0:
				move = get_str_response(prompt,combat_options)
				if move == "attack":
					attack_damage=base_damage*weapon_damage_multiplier*hero_damage_multiplier
					ehp=ehp-attack_damage
					counter+=1
					print "You heroically attack the %s for %f damage." % (monster,attack_damage)
					#Resets the monster damage multiplier to make sure that defend only lasts one round
					monster_damage_multiplier=1.0
				elif move == "defend":
					print "You ready yourself against the %s's next attack." % monster
					monster_damage_multiplier=.2
					counter+=1
				#Uses your potion
				elif move == "item":
					item=get_str_response(item_prompt,item_options)
					if item=="potion":
						if inventory[4]>0:
							print "You use a potion and restore hp. You feel restored."
							hp=90
							counter+=1
							inventory[4]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no potions left"
					#Uses you magic scroll
					elif item=="magic" or item == "scroll":
						if inventory[5]>0:
							print "You read the words off the magic scroll and suddenly a mighty lightning bolt",
							print " strikes your enemy for 50 damage."
							print "As you admire the damage the scroll dissolves in your hand."
							ehp=ehp-50
							counter+=1
							inventory[5]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no magic scrolls left."
				elif move == "run":
					print "You successfully escape from the %s" % monster
					output["run"]= True
					output["stats"][0]=hp
					return output
			#If counter is odd the Monster moves
			elif counter % 2 ==1:
				#Monsters have set attack patterns, well mostly set. The key is figuring out what they are and
				#what the best strategy is given their pattern.
				
				
				#Weak attack
				if decision % 3>0 and not enraged:
					print "The %s charges at you " % monster,
					#Calculates how much damage the attack does.
					damage=10*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "for %f damage." % damage
					if (ehp/100.0)<=.2:
						#Enrages the monster if hp is less than 20%
						enraged=True
						print "The %s has become enraged." % monster
					#hero_damage_multiplier=1.0 Monsters don't defend for now
					counter+=1
					decision+=1
				#Strong attack
				elif decision % 3==0 and not enraged:
					print "The %s swings at you with their swords" % monster,
					damage=30*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print " for %f damage." %damage
					counter+=1
					decision+=1
					if (ehp/100.0)<=.2:
						#Enrages the monster if hp is less than 20%
						enraged=True
						print "The %s has become enraged." % monster
				#This is your enraged attack.
				elif enraged:
					print "The %s are enraged and attack you with suicidle ferver." % monster
					damage=50*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "The %s deals a massive %f damage." % (monster, damage)
					counter+=1
		#Displays/computs the following if the monster kills you.
		if hp <= 0:
			print "The %s has defeated  you. You have failed in your" % monster,
			print "quest for the Master Sword. Better luck next time."
			print "                    Game Over                    "
			exit(0)
		
		#Displays/computs the following if you kill the monster
		elif ehp<=0:
			print "Congratuations: You have felled the %s. As a reward you have received:" % monster
			#Next block of code determines your loot.
			output["inventory"]=loot(output["inventory"],1)
			output["stats"][0]=hp
			return output
	if enemy==2:
		monster="Swarm of Fire Bats"
		output["enemy"]=monster
		prompt="What's your next move against the %s?.\n" % monster
		print "You have a encountered %s. Time for battle!!\n" % monster
		
		#setting a counter. The allows the while loop to alernate between your move and the monters
		counter=0
		
		#These lines allow attacks to deal more or less damage. Defending/running away will changing these
		hero_damage_multiplier=1.0
		monster_damage_multiplier=1.0
		
		#Initializes the monsters moves
		enraged=False
		decision = 2
		
		
		#While loop in which the battle actually takes place
		while hp>0 and ehp>0:
			#If counter is Even, the hero moves
			if counter % 2==0:
				move = get_str_response(prompt,combat_options)
				if move == "attack":
					attack_damage=base_damage*weapon_damage_multiplier*hero_damage_multiplier
					ehp=ehp-attack_damage
					counter+=1
					print "You heroically attack the %s for %f damage." % (monster,attack_damage)
					#Resets the monster damage multiplier to make sure that defend only lasts one round
					monster_damage_multiplier=1.0
				elif move == "defend":
					print "You ready yourself against the %s's next attack." % monster
					monster_damage_multiplier=.2
					counter+=1
				#Uses your potion
				elif move == "item":
					item=get_str_response(item_prompt,item_options)
					if item=="potion":
						if inventory[4]>0:
							print "You use a potion and restore hp. You feel restored."
							hp=90
							counter+=1
							inventory[4]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no potions left"
					#Uses you magic scroll
					elif item=="magic" or item == "scroll":
						if inventory[5]>0:
							print "You read the words off the magic scroll and suddenly a mighty lightning bolt",
							print " strikes your enemy for 50 damage."
							print "As you admire the damage the scroll dissolves in your hand."
							ehp=ehp-50
							counter+=1
							inventory[5]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no magic scrolls left."
				elif move == "run":
					print "You successfully escape from the %s" % monster
					output["run"]= True
					output["stats"][0]=hp
					return output
			#If counter is odd the Monster moves
			elif counter % 2 ==1:
				#Monsters have set attack patterns, well mostly set. The key is figuring out what they are and
				#what the best strategy is given their pattern.
				
				#Fly attack
				if decision % 4==2 and not enraged:
					print "The %s fly up into the air" % monster
					#Fly up into the air to Swoop down for the next attack. Take not damage on the next attack.
					hero_damage_multiplier=0.0
					counter+=1
					decision+=1
				#Fly part 2	
				elif decision % 4 ==3 and not enraged:
					damage=40*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "The %s swoops down for %f damage." % (monster,damage)
					counter+=1
					decision+=1
					hero_damage_multiplier=1.0
					if (ehp/100.0)<=.2:
						enraged=True
						print "The %s has become enraged." % monster
				#Screech attack
				elif decision % 4 < 2 and not enraged:
					print "The %s crys at you with a powerful screech" % monster,
					damage=10*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print " for %f damage." %damage
					counter+=1
					decision+=1
					if (ehp/100.0)<=.2:
						#Enrages the monster if hp is less than 20%
						enraged=True
						print "The %s has become enraged." % monster
				#This is your enraged attack.
				elif enraged:
					print "The %s are enraged and attack with a wave of immolating fire." % monster
					damage=50*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "The %s deals a massive %f damage." % (monster, damage)
					counter+=1
		#Displays/computs the following if the monster kills you.
		if hp <= 0:
			print "The %s has defeated  you. You have failed in your" % monster,
			print "quest for the Master Sword. Better luck next time."
			print "                    Game Over                    "
			exit(0)
		
		#Displays/computs the following if you kill the monster
		elif ehp<=0:
			print "Congratuations: You have felled the %s. As a reward you have received:" % monster
			#Next block of code determines your loot.
			output["inventory"]=loot(output["inventory"],1)
			output["stats"][0]=hp
			return output
	if enemy==3:
		monster="Contingent of Skeletons"
		output["enemy"]=monster
		prompt="What's your next move against the %s?.\n" % monster
		print "You have a encountered %s. Time for battle!!\n" % monster
		
		#setting a counter. The allows the while loop to alernate between your move and the monters
		counter=0
		
		#These lines allow attacks to deal more or less damage. Defending/running away will changing these
		hero_damage_multiplier=1.0
		monster_damage_multiplier=1.0
		
		#Initializes the monsters moves
		enraged=False
		decision = 0
		
		
		#While loop in which the battle actually takes place
		while hp>0 and ehp>0:
			#If counter is Even, the hero moves
			if counter % 2==0:
				move = get_str_response(prompt,combat_options)
				if move == "attack":
					attack_damage=base_damage*weapon_damage_multiplier*hero_damage_multiplier
					ehp=ehp-attack_damage
					counter+=1
					print "You heroically attack the %s for %f damage." % (monster,attack_damage)
					#Resets the monster damage multiplier to make sure that defend only lasts one round
					monster_damage_multiplier=1.0
				elif move == "defend":
					print "You ready yourself against the %s's next attack." % monster
					monster_damage_multiplier=.2
					counter+=1
				#Uses your potion
				elif move == "item":
					item=get_str_response(item_prompt,item_options)
					if item=="potion":
						if inventory[4]>0:
							print "You use a potion and restore hp. You feel restored."
							hp=90
							counter+=1
							inventory[4]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no potions left"
					#Uses you magic scroll
					elif item=="magic" or item == "scroll":
						if inventory[5]>0:
							print "You read the words off the magic scroll and suddenly a mighty lightning bolt",
							print " strikes your enemy for 50 damage."
							print "As you admire the damage the scroll dissolves in your hand."
							ehp=ehp-50
							counter+=1
							inventory[5]-=1
							monster_damage_multiplier=1.0
						else:
							print "You have no magic scrolls left."
				elif move == "run":
					print "You successfully escape from the %s" % monster
					output["run"]= True
					output["stats"][0]=hp
					return output
			#If counter is odd the Monster moves
			elif counter % 2 ==1:
				#Monsters have set attack patterns, well mostly set. The key is figuring out what they are and
				#what the best strategy is given their pattern.
				
				
				#Weak attack
				if decision % 3>0 and not enraged:
					print "The horde of goblins charges at you ",
					#Calculates how much damage the attack does.
					damage=10*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "for %f damage." % damage
					if (ehp/100.0)<=.2:
						#Enrages the monster if hp is less than 20%
						enraged=True
					#hero_damage_multiplier=1.0 Monsters don't defend for now
					counter+=1
					decision+=1
				#Strong attack
				elif decision % 3==0 and not enraged:
					print "The %s swings at you with their swords" % monster,
					damage=30*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print " for %f damage." %damage
					counter+=1
					decision+=1
					if (ehp/100.0)<=.2:
						#Enrages the monster if hp is less than 20%
						enraged=True
						print "enraged"
				#This is your enraged attack.
				elif enraged:
					print "The %s are enraged and attack you with suicidle ferver." % monster
					damage=50*monster_damage_multiplier*armor_damage_reduction
					hp=hp-damage
					print "The %s deals a massive %f damage." % (monster, damage)
					counter+=1
		#Displays/computs the following if the monster kills you.
		if hp <= 0:
			print "The %s has defeated  you. You have failed in your" % monster,
			print "quest for the Master Sword. Better luck next time."
			print "                    Game Over                    "
			exit(0)
		
		#Displays/computs the following if you kill the monster
		elif ehp<=0:
			print "Congratuations: You have felled the %s. As a reward you have received:" % monster
			#Next block of code determines your loot.
			output["inventory"]=loot(output["inventory"],1)
			output["stats"][0]=hp
			return output
							
				
#inventory=[1,0,1,0,1,1]
#stats=[100.0,20.0]	

#outcome=monster_l1(inventory,stats)
#print outcome
		
		
