#This module has functions for getting responses from the users based on a finted amount of "correct responses"

#Module to get String reponses. Takes two inputs. The first is a str prompt that displays each time it asks
#for a response. The second is a dictonary with 2 keys. The first is "Help" and maps to a string that lists
#all the valid inputs. The second is "Valid_Inputs" and contains a list of list of all the str's the parent program
#accept as a valid input.
def get_str_response(prompt,responses):
	valid_response=False
	
	#Loop Until user inputs a valid response
	while valid_response==False:
		input=raw_input(prompt)
		input=input.lower()
		for item in responses["Valid_Inputs"]:
			if item in input:
				return item
		
		if "help" in input:
			for item in responses["Help"]:
				print item
		else:
			print "%s is not an option" % input 
			
			
#testing={
#"Help":["\nYour options are 1: Go Left","\t\t 2: Go Right","\t\t 3: Go Forwards", "\t\t 4: Go Backwards"],
#"Valid_Inputs":["left","right","forwards","backwards"]
#}

#prompt= "What will you do next: "

#for i in range(10):
#	response=get_str_response(prompt,testing)
	#print response