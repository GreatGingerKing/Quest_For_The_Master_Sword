from sys import exit
from random import randint
import time
from get_response import get_str_response
from monster_fight import monster_l1
from Room_Class import RoomLvL1, MasterRoom
from player_class import Player


# Generic dungeon room: Takes a move counter, an inventory list and and a Stat/attribute list.
def forest_room_1(counter, inventory, stats):
	#Quits games if too many moves have been made. Exits to make sure there's not memory leakage/also so game ends.
	counter+=counter
	if counter>1000:
		print "You have gotten lost in the woods and failed in your quest."
		print "          GAME    OVER         "
		exit(0)
		
	#place holder for Room into function
	location=room_introduction()
	l_prompt="It's time to move on from the %s, where will you go next?\n " % location
	#placeholder for the function that generates dungeon monster. Not every room will have one but,
	
	#I think it will apper before the player can choose which direction to go.
	#monster=monster_encounter(player,difficulty_lvl)
	
		
	#m_prompt="With the %s defeated, what will you do next?" % monster
	responses={
	"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
	"Valid_Inputs":["left","right","forwards","backwards"]
	}
		
	choice=get_str_response(l_prompt,responses)
	if choice=="left":
		return 5, counter, inventory, stats
	elif choice=="right":
		return 2, counter, inventory, stats
	elif choice == "forwards":
		return 10, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		
			

		
			
def forest_room_8(counter, inventory, stats):
	#Quits games if too many moves have been made. Exits to make sure there's not memory leakage/also so game ends.
	counter+=counter
	if counter>1000:
		print "You have gotten lost in the woods and failed in your quest."
		print "          GAME    OVER         "
		exit(0)
		
	#place holder for Room into function
	location=room_introduction()
	l_prompt="It's time to move on from the %s, where will you go next?\n " % location
	print "As you arrive in the %s you see some monsters up ahead. It's time to fight!"
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
	
	#This function is the one that fights the monster
	outcome=monster_l1(player)
	#Unpacks outcome. Outcomes Form is {"player,enemy,run"}
	inventory=outcome["inventory"]
	stats=outcome["stats"]
	monster=outcome["enemy"]
	m_prompt="With the %s defeated, what will you do next?\n" % monster
	
	#If you run away from a fight, you get sent in a random direction.
	if outcome["run"]==True:
		print "In your haste to get away, you don't look which way you were running",
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
	else:
		choice=get_str_response(m_prompt,responses)
		
	if choice == "left":
		return 7, counter, inventory, stats
	elif choice == "right":
		return 9, counter, inventory, stats
	elif choice == "forwards":
		return 14, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats

		
	
		
#This next bit of code is the big deal. The main while loop that runs the whole game. In theory. When this is done, 
#With a bit of tidying up, I'll have a working game. But fist let's initialize some variables

#First we're going to set up the inventory. As of now the items, in order are: Wooden sword, Iron sword, wooden shield
#Iron Shield, Potion, and magic scroll.
inventory=[1,0,1,0,2,1]
#Next's We're going to initiatlize both the move counter and the your base stats/vitals. Your base stats are, in order:
#Hp and base damage. We also start out in room 3.
stats=[200.0,20]
counter=0
#Initialize Player
david = Player(inventory, stats)
room_number=3
responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
#Initialize the forest rooms
forest_room_1=RoomLvL1(5,2,10,3,responses)
forest_room_2=RoomLvL1(1,3,9,3,responses)
forest_room_3=RoomLvL1(2,4,8,3,responses)
forest_room_4=RoomLvL1(3,5,9,3,responses)
forest_room_5=RoomLvL1(4,1,10,3,responses)
forest_room_6=RoomLvL1(15,7,11,1,responses)
forest_room_7=RoomLvL1(6,8,14,2,responses)
forest_room_8=RoomLvL1(7,9,14,4,responses)
forest_room_9=RoomLvL1(8,10,14,4,responses)
forest_room_10=RoomLvL1(9,20,14,8,responses)
forest_room_11=RoomLvL1(15,14,16,6,responses)
forest_room_12=RoomLvL1(21,13,15,24,responses)
forest_room_13=RoomLvL1(19,21,18,25,responses)
forest_room_14=RoomLvL1(15,15,15,15,responses)
forest_room_15=RoomLvL1(19,21,20,14,responses)
forest_room_16=RoomLvL1(24,17,21,14,responses)
forest_room_17=RoomLvL1(21,19,22,12,responses)
forest_room_18=RoomLvL1(23,25,25,25,responses)
forest_room_19=RoomLvL1(1,5,24,21,responses)
forest_room_20=RoomLvL1(24,21,19,9,responses)
forest_room_21=RoomLvL1(22,22,24,21,responses)
forest_room_22=RoomLvL1(19,24,25,21,responses)
forest_room_23=MasterRoom(responses)
forest_room_24=RoomLvL1(25,25,3,3,responses)
forest_room_25=RoomLvL1(25,25,25,25,responses)		

forest_rooms={1:forest_room_1, 2:forest_room_2, 3:forest_room_3, 4:forest_room_4, 5: forest_room_5,
              6:forest_room_6, 7:forest_room_7, 8:forest_room_8, 9:forest_room_9, 10: forest_room_10,
			  11:forest_room_11, 12:forest_room_12 , 13:forest_room_13, 14:forest_room_14, 15: forest_room_15,
			  16:forest_room_16, 17:forest_room_17, 18:forest_room_18, 19:forest_room_19, 20: forest_room_20,
			  21:forest_room_21, 22:forest_room_22, 23:forest_room_23, 24:forest_room_24, 25: forest_room_25
}
#Next part Greets the player with the text from opening.txt before the game starts

opening = open("opening.txt",'r')
opening_txt=opening.read()
print opening_txt
opening.close()
raw_input()

while room_number != 26:
	room_number, counter, david =forest_rooms[room_number].play(counter,david)




