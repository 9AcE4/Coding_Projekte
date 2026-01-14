#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from utility_plant import *
from utility_sensor import *
from utility_movement import *
from Movement import *
from preps import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#======================================================#
#	PLANTING
#======================================================#
#------------------------------------------------------#
#	basics
#------------------------------------------------------#
					## -- hay -- ##
def run_hay():
	snake(prep_hay)
					## -- wood -- ##
def run_wood():
	snake(prep_wood)
					## -- carrot -- ##
def run_carrot():
	snake(prep_carrot)
#------------------------------------------------------#
#	Companion (hay,wood,carrot)
#------------------------------------------------------#
def run_ran_com(random=False):
	
	if get_entity() == None:
		plant(Entities.Grass)
# - - data - - #
	old_x = get_pos_x()				# start x
	old_y = get_pos_y()				# start y
	com_x = get_companion()[1][0]	# companion x
	com_y = get_companion()[1][1]	# companion y
	com_e = get_companion()[0]		# companion entity
	
# - - goto companion spot and prepare - - #
	goto(com_x,com_y)
	if get_entity() != com_e:
		harv()
		till_soil()
		plant(com_e)
	if random == True:
		full_water()
		
# - - go back and harvest - - #
	goto(old_x,old_y)
	harv_wait()
	if random == False:
		till_soil()
		if low_com() == Entities.Tree:
			plant(Entities.Bush)
		else:
			plant(low_com())
		
# - - back to companion - - #
	elif random == True:
		goto(com_x,com_y)

#------------------------------------------------------#
#	Pumpkin
#------------------------------------------------------#
def run_pumpkin():

	phase1 = True
	phase2 = False
	phase3 = False
	
## -- PHASE 1 -- ##
	while phase1 == True:
		
		snake(prep_pumpkin)
		
		phase1 = False
		phase2 = True
	
## -- PHASE 2 -- #
	while phase2 == True:
		
		replant = []
		
		def replant_list():
			if plant(Entities.Pumpkin):
				replant.append((get_x(),get_y()))
		
		wrap_snake(replant_list)
			
		if len(replant) <= 200:		# < change limit

			phase2 = False
			phase3 = True
			
## -- PHASE 3 -- #
	while phase3 == True:
		
		goto(replant[0][0],replant[0][1])
		
		while can_harvest() == False:
			plant(Entities.Pumpkin)
			smart_water()
			
		if can_harvest() == True:
			replant.pop(0)
			
		if len(replant) == 0:
			goto(0,0)
			harv()
			phase1 = True
			phase3 = False
			
#------------------------------------------------------#
#	Sunflower / Power
#------------------------------------------------------#
def run_power():
## -- liste aller sunflowers -- ##
	blüten =	{			
					15	:	[],		# koordinaten mit 15 blüten
					14	:	[],		# koordinaten mit 14 blüten
					13	:	[],		# koordinaten mit 13 blüten
					12	:	[],		# koordinaten mit 12 blüten
					11	:	[],		# koordinaten mit 11 blüten
					10	:	[],		# koordinaten mit 10 blüten
					 9	:	[],		# koordinaten mit  9 blüten
					 8	:	[],		# koordinaten mit  8 blüten
					 7	:	[]		# koordinaten mit  7 blüten
				}
				
	def prep_power():
		prep_sunflower()
		blüten[measure()].append((get_pos_x(), get_pos_y()))
						
	plantmode	= True
	harvmode	= False
	
	while plantmode == True:
		wrap_snake(prep_power)
		plantmode = False
		harvmode = True
	
	while harvmode == True:
		for anzahl in range(15,6,-1):			
			while blüten[anzahl]:					
				(tx,ty) = blüten[anzahl].pop(0)
				goto(tx,ty)									
				harv_wait()
		plantmode = True
		harvmode = False
		
#------------------------------------------------------#
#	Cactus
#------------------------------------------------------#
def run_cactus():

# phase: >> plant + pre-sort <<
	
	phase_plant = True
	phase_sort = False
	
	while phase_plant == True:
		snake(prep_cactus)
	
		phase_plant = False
		phase_sort = True
	
	
# phase: >> full sort + harv <<
	
	while phase_sort == True:
		if wrap_snake(sort) == 0:
			harv()
			
			phase_plant = True
			phase_sort = False
			
