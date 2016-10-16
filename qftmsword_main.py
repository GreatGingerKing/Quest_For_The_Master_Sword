from sys import exit
from random import randint
import time
from get_response import get_str_response
from monster_fight import monster_l1

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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
		
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
		
			
def forest_room_2(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	     
	#m_prompt="With the %s defeated, what will you do next?" % monster
	responses={
	"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
	"Valid_Inputs":["left","right","forwards","backwards"]
	}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 1, counter, inventory, stats
	elif choice == "right":
		return 3, counter, inventory, stats
	elif choice == "forwards":
		return 9, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		

def forest_room_3(counter, inventory, stats):
	#Quits games if too many moves have been made. Exits to make sure there's not memory leakage/also so game ends.
	counter+=counter
	if counter>1000:
		print "You have gotten lost in the woods and failed in your quest."
		print "          GAME    OVER         "
		exit(0)
		
	#place holder for Room into function
	location=room_introduction()
	l_prompt="It's time to move on from the %s, where will you go next?\n" % location
	
	#placeholder for the function that generates dungeon monster. Not every room will have one but,
	#I think it will apper before the player can choose which direction to go.
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
	"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
	"Valid_Inputs":["left","right","forwards","backwards"]
	}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 2, counter, inventory, stats
	elif choice == "right":
		return 4, counter, inventory, stats
	elif choice == "forwards":
		return 8, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		

def forest_room_4(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
	"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
	"Valid_Inputs":["left","right","forwards","backwards"]
	}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 3, counter, inventory, stats
	elif choice == "right":
		return 5, counter, inventory, stats
	elif choice == "forwards":
		return 9, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		
			
def forest_room_5(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 4, counter, inventory, stats
	elif choice == "right":
		return 1, counter, inventory, stats
	elif choice == "forwards":
		return 10, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		
			
def forest_room_6(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 15, counter, inventory, stats
	elif choice == "right":
		return 7, counter, inventory, stats
	elif choice == "forwards":
		return 11, counter, inventory, stats
	elif choice == "backwards":
		return 1, counter, inventory, stats
		
			
def forest_room_7(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 6, counter, inventory, stats
	elif choice == "right":
		return 8, counter, inventory, stats
	elif choice == "forwards":
		return 14, counter, inventory, stats
	elif choice == "backwards":
		return 2, counter, inventory, stats
		
			
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
        print "As you arrive in the %s you see some monsters up ahead. It's time to fight!" % location
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
	
	#This function is the one that fights the monster
	outcome=monster_l1(inventory,stats)
	#Unpacks outcome. Outcomes Form is {"inventory,stats,enemy,run"}
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
		
			
def forest_room_9(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 8, counter, inventory, stats
	elif choice == "right":
		return 10, counter, inventory, stats
	elif choice == "forwards":
		return 14, counter, inventory, stats
	elif choice == "backwards":
		return 4, counter, inventory, stats
		
			
def forest_room_10(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 9, counter, inventory, stats
	elif choice == "right":
		return 20, counter, inventory, stats
	elif choice == "forwards":
		return 14, counter, inventory, stats
	elif choice == "backwards":
		return 8, counter, inventory, stats
		
			
def forest_room_11(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 15, counter, inventory, stats
	elif choice == "right":
		return 14, counter, inventory, stats
	elif choice == "forwards":
		return 16, counter, inventory, stats
	elif choice == "backwards":
		return 6, counter, inventory, stats
		
			
def forest_room_12(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 21, counter, inventory, stats
	elif choice == "right":
		return 13, counter, inventory, stats
	elif choice == "forwards":
		return 15, counter, inventory, stats
	elif choice == "backwards":
		return 24, counter, inventory, stats
		
def forest_room_13(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 19, counter, inventory, stats
	elif choice == "right":
		return 21, counter, inventory, stats
	elif choice == "forwards":
		return 18, counter, inventory, stats
	elif choice == "backwards":
		return 25, counter, inventory, stats
		
			
def forest_room_14(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 15, counter, inventory, stats
	elif choice == "right":
		return 15, counter, inventory, stats
	elif choice == "forwards":
		return 15, counter, inventory, stats
	elif choice == "backwards":
		return 15, counter, inventory, stats
		
def forest_room_15(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 19, counter, inventory, stats
	elif choice == "right":
		return 21, counter, inventory, stats
	elif choice == "forwards":
		return 20, counter, inventory, stats
	elif choice == "backwards":
		return 14, counter, inventory, stats
		
			
def forest_room_16(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 24, counter, inventory, stats
	elif choice == "right":
		return 17, counter, inventory, stats
	elif choice == "forwards":
		return 21, counter, inventory, stats
	elif choice == "backwards":
		return 14, counter, inventory, stats
		
			
def forest_room_17(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
	
	choice=get_str_response(l_prompt,responses)
	
	if choice == "left":
		return 21, counter, inventory, stats
	elif choice == "right":
		return 19, counter, inventory, stats
	elif choice == "forwards":
		return 22, counter, inventory, stats
	elif choice == "backwards":
		return 12, counter, inventory, stats
		
		
			
def forest_room_18(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 23, counter, inventory, stats
	elif choice == "right":
		return 25, counter, inventory, stats
	elif choice == "forwards":
		return 25, counter, inventory, stats
	elif choice == "backwards":
		return 25, counter, inventory, stats
		
			
def forest_room_19(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 1, counter, inventory, stats
	elif choice == "right":
		return 5, counter, inventory, stats
	elif choice == "forwards":
		return 24, counter, inventory, stats
	elif choice == "backwards":
		return 21, counter, inventory, stats
		
			
def forest_room_20(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 24, counter, inventory, stats
	elif choice == "right":
		return 21, counter, inventory, stats
	elif choice == "forwards":
		return 19, counter, inventory, stats
	elif choice == "backwards":
		return 19, counter, inventory, stats
		
			
def forest_room_21(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 22, counter, inventory, stats
	elif choice == "right":
		return 22, counter, inventory, stats
	elif choice == "forwards":
		return 24, counter, inventory, stats
	elif choice == "backwards":
		return 21, counter, inventory, stats
		
			
def forest_room_22(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 19, counter, inventory, stats
	elif choice == "right":
		return 24, counter, inventory, stats
	elif choice == "forwards":
		return 25, counter, inventory, stats
	elif choice == "backwards":
		return 21, counter, inventory, stats
		
			
def master_sword_room(counter, inventory, stats):
	#Quits games if too many moves have been made. Exits to make sure there's not memory leakage/also so game ends.
	counter+=counter
	if counter>1000:
		print "You have gotten lost in the woods and failed in your quest."
		print "          GAME    OVER         "
		#exit(0)
		
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
	
	return 26, counter, inventory, stats
		
			
def forest_room_24(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 25, counter, inventory, stats
	elif choice == "right":
		return 25, counter, inventory, stats
	elif choice == "forwards":
		return 3, counter, inventory, stats
	elif choice == "backwards":
		return 3, counter, inventory, stats
		
			
def forest_room_25(counter, inventory, stats):
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
	#monster=monster_encounter(inventory,stats,difficulty_lvl)
	
	#m_prompt="With the %s defeated, what will you do next?" % monster
	
	responses={
		"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
		"Valid_Inputs":["left","right","forwards","backwards"]
		}
		
	choice=get_str_response(l_prompt,responses)
		
	if choice == "left":
		return 25, counter, inventory, stats
	elif choice == "right":
		return 25, counter, inventory, stats
	elif choice == "forwards":
		return 25, counter, inventory, stats
	elif choice == "backwards":
		return 25, counter, inventory, stats
		
#This next function is the room switcher/hallway. It handles the movement between the rooms and is called by
#main loop of the program. This was suggested, kindly, by Jon as a way to avoid memory leaking.

def forest_room_switcher(room_number,counter,inventory,stats):
	#Initialze destination
	destination=0
	if room_number==1:
		destination, counter, inventory, stats=forest_room_1(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==2:
		destination, counter, inventory, stats=forest_room_2(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==3:
		destination, counter, inventory, stats=forest_room_3(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==4:
		destination, counter, inventory, stats=forest_room_4(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==5:
		destination, counter, inventory, stats=forest_room_5(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==6:
		destination, counter, inventory, stats=forest_room_6(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==7:
		destination, counter, inventory, stats=forest_room_7(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==8:
		destination, counter, inventory, stats=forest_room_8(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==9:
		destination, counter, inventory, stats=forest_room_9(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==10:
		destination, counter, inventory, stats=forest_room_10(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==11:
		destination, counter, inventory, stats=forest_room_11(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==12:
		destination, counter, inventory, stats=forest_room_12(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==13:
		destination, counter, inventory, stats=forest_room_13(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==14:
		destination, counter, inventory, stats=forest_room_14(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==15:
		destination, counter, inventory, stats=forest_room_15(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==16:
		destination, counter, inventory, stats=forest_room_16(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==17:
		destination, counter, inventory, stats=forest_room_17(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==18:
		destination, counter, inventory, stats=forest_room_18(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==19:
		destination, counter, inventory, stats=forest_room_19(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==20:
		destination, counter, inventory, stats=forest_room_20(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==21:
		destination, counter, inventory, stats=forest_room_21(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==22:
		destination, counter, inventory, stats=forest_room_22(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==23:
		destination, counter, inventory, stats=master_sword_room(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==24:
		destination, counter, inventory, stats=forest_room_24(counter,inventory,stats)
		return destination, counter, inventory, stats
	if room_number==25:
		destination, counter, inventory, stats=forest_room_25(counter,inventory,stats)
		return destination, counter, inventory, stats
	
		
#This next bit of code is the big deal. The main while loop that runs the whole game. In theory. When this is done, 
#With a bit of tidying up, I'll have a working game. But fist let's initialize some variables

#First we're going to set up the inventory. As of now the items, in order are: Wooden sword, Iron sword, wooden shield
#Iron Shield, Potion, and magic scroll.
inventory=[1,0,1,0,0,0]
#Next's We're going to initiatlize both the move counter and the your base stats/vitals. Your base stats are, in order:
#Hp and base damage. We also start out in room 3.
stats=[100.0,20]
counter=0
room_number=3

#Next part Greets the player with the text from opening.txt before the game starts

opening = open("opening.txt",'r')
opening_txt=opening.read()
print opening_txt
opening.close()
raw_input()

while room_number != 26:
	room_number, counter, inventory, stats=forest_room_switcher(room_number, counter, inventory, stats)




