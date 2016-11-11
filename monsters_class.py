class Monster(object):
	hp=100
	max_hp=100
	weak_attack=10.0
	strong_attack=30.0
	enraged_attack=50.0
	counter=0
	monster_damage_reduction=1.0
	Enraged = False
	def __init__(self,name):
		self.name=name
		
	#This function is the the A.I for the Monster. It's pretty simple. However this is
	#is just meant as a staring point.
	def attack(self,armor_damage_reduction,monster_damage_multiplier):
		#Monsters have set attack patterns, well mostly set. The key is figuring out what they are and
		#what the best strategy is given their pattern.
		if (self.counter==0 or self.counter % 4==0) and not self.Enraged:
			self.counter+=1
			print "The %s strongly attacks you" % self.name,
			damage=self.strong_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." % damage
			#Monsters become enraged once their HP becomes less than 20% of max
			#However, you get a 1 turn warning of this.
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self. name
				self.Enraged = True
			return damage
		elif self.counter % 4 != 0  and not self.Enraged:
			self.counter+=1
			print "The %s weakly attacks you" % self.name,
			damage=self.weak_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." %damage
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self.name
				self.Enraged = True
			return damage
		elif self.hp <= .2*self.max_hp and self.Enraged:
			print "The %s attacks you enraged." % self.name,
			damage=self.enraged_attack*armor_damage_reduction*monster_damage_multiplier
			print "The %s deals a massive %f damage." % (self.name, damage)
			return damage
			
class Goblin(Monster):
	counter=1
	def __init__(self):
	    self.name="Pack of Goblins"
	
	def attack(self, armor_damage_reduction, monster_damage_multiplier):
		if (self.counter==0 or self.counter % 3==0) and not self.Enraged:
			self.counter+=1
			print "The %s swings at you with their swords" %  self.name,
			damage=self.strong_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." % damage
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self. name
				self.Enraged = True
			return damage
		elif self.counter % 3 != 0  and not self.Enraged:
			self.counter+=1
			print "The %s charges at you"  % self.name,
			damage=self.weak_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." %damage
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self. name
				self.Enraged = True
			return damage
		elif self.hp < .2*self.max_hp and self.Enraged:
			print "The %s are enraged and attack you with suicidle ferver." % self.name
			damage=self.enraged_attack*armor_damage_reduction*monster_damage_multiplier
			print "The %s deals a massive %f damage." % (self.name, damage)
			return damage
			
class FireBat(Monster):
	strong_attack=40.0
	counter = 2
	
	def __init__(self):
		self.name="Swarm of Fire Bats"
	
	def attack(self, armor_damage_reduction, monster_damage_multiplier):
		if self.counter % 4 == 2 and not self.Enraged:
			self.counter+=1
			print "The %s fly up into the air" % self.name
			damage =0
			self.monster_damage_reduction=0.0
			return damage
		elif self.counter % 4 == 3:
			self.counter+=1
			damage=self.strong_attack*armor_damage_reduction*monster_damage_multiplier
			print "The %s swoops down for %f damage." % (self.name,damage)
			self.monster_damage_reduction=1.0
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self. name
				self.Enraged = True
			return damage
		elif self.counter % 4 <2 and not self.Enraged:
			self.counter+=1
			damage=self.weak_attack*armor_damage_reduction*monster_damage_multiplier
			print "The %s screech at you for %f damage." % (self.name,damage)
			if self.hp <= .2*self.max_hp and not self.Enraged:
				print "The %s has become enraged." % self. name
				self.Enraged = True
			return damage
		elif self.hp < .2*self.max_hp and self.Enraged:
			 print "The %s are enraged and attack with a wave of immolating fire." % self.name
			 damage=self.enraged_attack*armor_damage_reduction*monster_damage_multiplier
			 print "The %s deals a massive %f damage." % (self.name, damage)
			 return damage
			 
class Skeleton(Monster):

	def __init__(self):
		self.name="Contingent of Skeletons"
		
	def attack(self, armor_damage_reduction, monster_damage_multiplier):
		if (self.counter == 0 or self.counter % 3 ==0) and self.hp >= .2*self.max_hp:
			self.counter+=1
			print "The %s smash at you with its boney club" % self.name,
			damage=self.strong_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." % damage
			return damage
		elif self.counter %3 != 0 and self.hp >= .2*self.max_hp:
			self.counter+=1
			print "A %s claw at you" % self.name,
			damage=self.weak_attack*armor_damage_reduction*monster_damage_multiplier
			print "for %f damage." % damage
			return damage
		#Skelton's don't get angry. They just get even. 
		elif self.hp < .2*self.max_hp:
			print "The %s reassbles itself gaining 50 health." %self.name
			self.hp+=50
			return 0.0
		
			
		
		
		
#rodger=Monster("Goblins")
#adr=1.0
#mdm=1.0
#print rodger.hp, rodger.weak_attack, rodger.strong_attack
#print rodger.enraged_attack
#print rodger.name, rodger.counter

#while rodger.hp>0:
	#print rodger.attack(adr,mdm)
	#rodger.hp-=10
	#print rodger.hp

	
#Krenko = Goblin()

#while Krenko.hp>0:
	#print Krenko.attack(adr, mdm)
	#Krenko.hp-=10
	
#Zubat =FireBat()

#while Zubat.hp>0:
	#print Zubat.attack(adr,mdm)
	#Zubat.hp-=10
	
#Bones= Skeleton()

#while Bones.hp>0:
	#print Bones.attack(adr,mdm)
	#Bones.hp-=21