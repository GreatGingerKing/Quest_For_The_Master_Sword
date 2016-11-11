#This Module contains funtions for fighting monsters of differnt levels. All levels
#Require your inventory, and your stats.
from random import randint, random
from get_response import get_str_response
from sys import exit
from loot import loot
from monsters_class import Monster, Goblin, FireBat, Skeleton
from player_class import Player

def monster_l1(david):
	#Pulls your Statistics from stats
	hp=david.stats[0]
	base_damage=david.stats[1]
	
	#Here we prime the out put of our function being a dictionary. The fist key is out inventory, the second our stats,
	#The third, the type of monster, and the fourth the boolean false value. This is used for when we run. The parent
	#function will check this. If true, if will generate a random room to go to instead of the usual ones.
	output={"inventory":david.inventory,"stats":david.stats,"enemy":"","run":False}
	
	#Sets monster hp
	ehp=100.0
	
	#This next statement checks to see what weapon you have and sets your damage multiplier
	if david.inventory[1]==1:
		weapon_damage_multiplier=1.5
	else:
		weapon_damage_multiplier=1.0
		
	#This next statment checks to seet what shield you have sets the armor damage reduction
	
	if david.inventory[3]==1:
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
	enemy=randint(1,3)
	#enemy=1
	
	#Initializes the enemy based on what the roll was.
	#Monsters are named Rodger. Who knows why.
	if enemy==1:
		monster="Pack of goblins"
		Rodger = Goblin()
	
	elif enemy == 2:
		monster = "Swarm of Fire Bats"
		Rodger = FireBat()
	
	elif enemy ==3:
		monster = "Contingent of Skeletons"
		Rodger = Skeleton()
		
	output["enemy"]=monster	
	prompt="What's your next move against the %s?.\n" % monster
	print "You have a encountered %s. Time for battle!!\n" % monster
		
	#setting a counter. The allows the while loop to alernate between your move and the monters
	counter=0
		
	#These lines allow attacks to deal more or less damage. Defending/running away will changing these
	monster_damage_multiplier=1.0
		

		
	#While loop in which the battle actually takes place
	while hp>0 and Rodger.hp>0:
		#If counter is Even, the hero moves
		if counter % 2==0:
			#Asks the david for the move.
			move = get_str_response(prompt,combat_options)
			if move == "attack":
				attack_damage=(base_damage*weapon_damage_multiplier
				               *Rodger.monster_damage_reduction)
				Rodger.hp=Rodger.hp-attack_damage
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
					if david.inventory[4]>0:
						print "You use a potion and restore hp. You feel restored."
						hp=90
						counter+=1
						david.inventory[4]-=1
						monster_damage_multiplier=1.0
					else:
						print "You have no potions left"
				#Uses you magic scroll
				elif item=="magic" or item == "scroll":
					if david.inventory[5]>0:
						print "You read the words off the magic scroll and suddenly a mighty lightning bolt",
						print " strikes your enemy for 50 damage."
						print "As you admire the damage the scroll dissolves in your hand."
						Rodger.hp=Rodger.hp-50
						counter+=1
						david.inventory[5]-=1
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
				
			#Monster damage is reduced by your armor and if you defended/unsucessrfully ran away.
			monster_damage=Rodger.attack(armor_damage_reduction, monster_damage_multiplier)
			hp=hp-monster_damage
			counter+=1
				
	#Displays/computs the following if the monster kills you.
	if hp <= 0:
		print "The %s has defeated  you. You have failed in your" % monster,
		print "quest for the Master Sword. Better luck next time."
		print "                    Game Over                    "
		exit(0)
		
	#Displays/computs the following if you kill the monster
	elif Rodger.hp<=0:
		print "Congratuations: You have felled the %s. As a reward you have received:" % monster
		#Next block of code determines your loot.
		output["inventory"]=loot(output["inventory"],1)
		output["stats"][0]=hp
		return output

				
"""david=Player([1,0,1,0,1,1],[100.0,20.0])


outcome=monster_l1(david)
print outcome"""
		
		
