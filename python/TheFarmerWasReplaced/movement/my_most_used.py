#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from utility_movement import *
from utility_fallbacks import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#==========================================================================#
#	B A S I C 
#==========================================================================#
#--------------------------------------------------------------------------#
#	basic pattern 
#--------------------------------------------------------------------------#
def just_north(func):
	for y in range(get_world_size()):
		
		func()
		
		move(North)
#--------------------------------------------------------------------------#
#	basic pattern 
#--------------------------------------------------------------------------#
def base_move(func):
	for x in range(get_world_size()):
		for y in range(get_world_size()):
				
			func()
			
			move(North)
		move(East)
		
#--------------------------------------------------------------------------#
#	basic pattern 
#--------------------------------------------------------------------------#
def mini(func):
	func()
	move(North)
	func()
	move(East)
	func()
	move(South)
	func()
	move(West)
#--------------------------------------------------------------------------#
#	Snake ( with jump )
#--------------------------------------------------------------------------#
def wrap_snake(func):
	
	counter = 0
		
	for move_east in range(get_world_size()):
		for move_north in range(get_world_size()-1):
			
			if get_pos_x() % 2 == 0:
				
				if func() == True:	#Aktion
					counter += 1
				
				move(North)
				
			else:
				
				if func() == True:	# Aktion
					counter += 1
				
				move(South)
				
		if func() == True:	# Aktion
			counter += 1
				
		move(East)
		
	return counter
			
		
#==========================================================================#
#	A D V A N C E D
#==========================================================================#
#--------------------------------------------------------------------------#
#	Snake ( no jump )
#--------------------------------------------------------------------------#

def snake(func=None):
	
	for move_east_west in range(get_world_size()):
		
		if get_pos_x() == 0:
			for move_north in range(get_world_size()-1):
				
				if func != None:
					func()	
				
				if move(North) == False and func == None:
					snake_reset()
					break
				
		elif get_pos_x() % 2 == 0 and get_pos_x() != 0:
			for move_north in range(get_world_size()-2):
				
				if func != None:
					func() 
				
				if move(North) == False and func == None:
					snake_reset()
					break
				
				
		elif get_pos_x() == get_world_size() -1:
			for move_south in range(get_world_size()-1):
				
				if func != None:
					func()	
				
				if move(South) == False and func == None:
					snake_reset()
					break
						
		else:
			if get_pos_x() % 2 != 0 and get_pos_x() != get_world_size() -1:
				for move_south in range(get_world_size()-2):
					
					if func != None:
						func()	
					
					if move(South) == False and func == None:
						snake_reset()
						break
					
		if get_pos_x() != get_world_size() -1 :
			
			if func != None:
				func()	
			
			if move(East) == False and func == None:
				snake_reset()
				break
			
		else:
			while get_pos_x() > 0 :
				
				if func != None:
					func()	
				
				if move(West) == False and func == None:
					snake_reset()
					break
