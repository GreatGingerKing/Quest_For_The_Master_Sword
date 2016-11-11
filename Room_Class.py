from random import randint
from get_response import get_str_response
from monster_fight import monster_l1
from sys import exit
from loot import loot
from player_class import Player
import time

#Function to randomly generate room intro.
def room_introduction():
	room_intro=""
	rand1=randint(1,3)
	
	if rand1==1:
		room_intro+="As you go deeper into the woods, "
	elif rand1==2:
		room_intro+="Continuing your journey through the forest, "
	elif rand1==3:
		room_intro+="Carrying on with your quest, "
	
	rand2=randint(1,3)
	
	if rand2==1:
		room_intro+="you stumble upon "
	elif rand2==2:
		room_intro+="you come across "
	elif rand2==3:
		room_intro+="you suddenly discover "
		
	rand3=randint(1,6)
	if rand3==1:
		location="grove"
		room_intro+="a vibrant grove."
	elif rand3==2:
		location="clearing"
		room_intro+="a sun-lit clearing."
	elif rand3==3:
		location="thicket"
		room_intro+="a dense thicket."
	elif rand3==4:
		location="stream"
		room_intro+="a vibrant stream."
	elif rand3==5:
		location="glade"
		room_intro+="a beautiful glade."
	elif rand3==6:
		location="lake"
		room_intro+="a shimmering lake."
	
	print room_intro
	return location

class RoomLvL1(object):

	#initializes which room each direction leads too, as well as the response dictionary.
	def __init__(self,left,right,forwards,backwards,responses):
		self.left=left
		self.right=right
		self.forwards=forwards
		self.backwards=backwards
		self.responses=responses
		
	def encounter(self,player, location):
		#This function randomly shoots to an "encounter" 
		situation=randint(1,3)
		#situation = 3
		if situation== 1:
			choice, player=self.monster_encounter(player, location)
			return choice, player
		elif situation == 2:
			choice, player = self.loot_encounter(player, location)
			return choice, player
		elif situation == 3:
			choice, player = self.challenge_encounter(player, location)
			return choice, player
		else:
			print "Crittical error, exiting"
			exit(0)
			
	def monster_encounter(self,player,location):
		#This function is the one that handles all the legwork for monters encounters insofar
		# as logistics is concerned.
		print "As you arrive in the %s you see some monsters up ahead. It's time to fight!" %location
		outcome=monster_l1(player)
		#Unpacks outcome. Outcome,s Form is {"inventory,stats,enemy,run"}
		player.inventory=outcome["inventory"]
		player.stats=outcome["stats"]
		monster=outcome["enemy"]
		#print monster
		m_prompt="With the %s defeated, what will you do next?\n" % monster
		
		#If you run away from a fight, you get sent in a random direction.
		if outcome["run"]==True:
			print "In your haste to get away, you don't have time to think about your choice",
			direction=randint(1,4)
			if direction==1:
				choice="left"
				print " and you run to your %s." % choice
			elif direction==2:
				choice="right"
				print " and you run to your %s." % choice
			elif direction==3:
				choice="backwards"
				print " and you run to your %s." % choice
			elif direction==4:
				choice="forwards"
				print " and you run to your %s." % choice
		#Else, Player gets to choose their direction.
		else:
			choice=get_str_response(m_prompt,self.responses)
			
		return choice, player
		
	def loot_encounter(self, player, location):
		#This encounter 
		print "As you arrive in the %s you see a treasure chest in front of you." % location
		print "You slowly open it to find...\n"
		player.inventory=loot(player.inventory,1)
		#print player.inventory
		
		#get player's choice for what's next
		loot_prompt="With your loot in hand it's time to move on. What will you do next?\n"
		choice=get_str_response(loot_prompt,self.responses)
		
		return choice, player
		
	def challenge_encounter(self, player,location):
		print "As you arrive in the %s you are greated by the towering sight of Great Sphinx." % location
		print '"Best my Challenge and be rewarded"'
		print '"But fail and you will find your journey cut short."'
		chal_prompt="With the Sphinx's riddle solved, It's time to move on. What will you do next?\n"
		#Dictionary of Challenges.
		challenges = {0:["""'This is a thing that is devoured by all things; flowers, trees, beasts, birds;
		bites steel, gnaws iron; grinds hard stone to meal;
		beats mountain down, ruins town and slays king. 
		What is it?': ""","time"]}
		#These two lines choose a random challenge to do.
		options = challenges.keys()
		situation=randint(1,len(options))
		#These lines execute the challenge
		#You get 3 Guesses
		guesses=3
		#Boolean for if you've guess right
		solved = False
		print '"I shall grant you three guesses now; Answer me this:"'
		print challenges[situation-1][0]
		answer=challenges[situation-1][1]
		#loop for getting guesses
		while guesses >0:
			guess = raw_input(">:")
			if answer in guess:
				solved = True
				break
			else:
				print "That is not correct, guess again."
				guesses-=1
		if solved == True:
			print "You have completed my challenge by answering my riddle."
			print "As a reward I shall allow you to proceed as well as give you this treasure chest."
			print "You open the chest to find..."
			player.inventory=loot(player.inventory,1)
			#Choose where to go next.
			choice=get_str_response(chal_prompt,self.responses)
			
			return choice, player
		else:
			print "You have failed to solve my riddle and your quest ends here."
			print "You need both strengh and intelligence to be a true hero."
			print                   "Game Over."
			exit(0)
			
		
	def play(self,counter,player):
		#This handles the overall running through the room. This is the "main" room function within this class.
		#Quits games if too many moves have been made. Exits to make sure there's not memory leakage/also so game ends.
		counter+=counter
		if counter>1000:
			print "You have gotten lost in the woods and failed in your quest."
			print "          GAME    OVER         "
			exit(0)
		
		#Room introduction function.
		location=room_introduction()
		#Call the encounter function to randomly encounter something.
		choice, player = self.encounter(player,location)
		#Moves the Player On depending on 'choice' was returned
		if choice == "left":
			return self.left, counter, player
		elif choice == "right":
			return self.right, counter, player
		elif choice == "forwards":
			return self.forwards, counter, player
		elif choice == "backwards":
			return self.backwards, counter, player
		else:
			print "Serious flaw detected, exited game."
			exit(0)
#This is the room for the master sword			
class MasterRoom(RoomLvL1):
	#Takes no inputs.
	def __init__(self, responses):
		self.left=3
		self.right=3
		self.forwards=3
		self.backwards=3
		self.respsonses=responses
		
	def play(self, counter,player):
		counter+=counter
		if counter>1000:
			print "You have gotten lost in the woods and failed in your quest."
			print "          GAME    OVER         "
			exit(0)
		#Reads from ending.txt to give the player a congradulatory diaglouge for ending the game.
		ending = open("ending.txt", 'r')
		txt_counter=0
	
	
		for i in range(17):
			if i==0:
				txt=ending.readline()
				print txt
				time.sleep(4)
			elif i>0 and i<12:
				txt=ending.readline()
				print txt
			elif i==12:
				txt=ending.readline()
				print txt
				time.sleep(4)
			else:
				txt=ending.readline()
				print txt
				time.sleep(.5)
		ending.close()
	
		return 26, counter, player
	
	
"""david=Player([1,0,1,0,0,0],[100.0,20])
print david.inventory
print david.stats
room8=RoomLvL1(7,9,10,3,{
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		})
counter=0
direction=0
direction, counter, player = room8.play(counter,david)
print direction
room23=MasterRoom({
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		})
direction, counter, player = room23.play(counter, david)
print direction"""