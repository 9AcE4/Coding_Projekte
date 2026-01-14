#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from utility_plant import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#=============================================================#
#	B A S I C
#=============================================================#
#-------------------------------------------------------------#
#	Hay
#-------------------------------------------------------------#
def prep_hay():
	harv()
	plant(Entities.Grass)
#-------------------------------------------------------------#
#	Bush
#-------------------------------------------------------------#
def prep_bush():
	harv()
	plant(Entities.Bush)
	smart_water()
#-------------------------------------------------------------#
#	Tree
#-------------------------------------------------------------#
def prep_tree(dung=False):
	harv()
	plant(Entities.Tree)
	smart_water()
	if dung == True:
		fertilize()
#-------------------------------------------------------------#
#	Carrot
#-------------------------------------------------------------#
def prep_carrot():
	harv_wait()
	till_soil()
	plant(Entities.Carrot)
	smart_water()
#-------------------------------------------------------------#
#	Pumpkin
#-------------------------------------------------------------#
def prep_pumpkin():
	harv()
	till_soil()
	plant(Entities.Pumpkin)
	smart_water()
#-------------------------------------------------------------#
#	Sunflower
#-------------------------------------------------------------#
def prep_sunflower():
	if get_entity_type() == None:
		pass
	else:
		harv_wait()
	till_soil()				
	plant(Entities.Sunflower)
	smart_water()
#-------------------------------------------------------------#
#	Cactus
#-------------------------------------------------------------#
def prep_cactus():
	harv()
	till_soil()
	plant(Entities.Cactus)
	sort()
	
#=============================================================#
#	A D V A N C E D
#=============================================================#
#-------------------------------------------------------------#
#	Wood
#-------------------------------------------------------------#	
def prep_wood():
	if (get_pos_x() + get_pos_y()) % 2 != 0:
		prep_tree()							
	else:
		prep_bush()
		
#-------------------------------------------------------------#
#	Cactus
#-------------------------------------------------------------#
	
def sort():
	
	posx = get_pos_x()
	posy = get_pos_y()
	sizew= get_world_size()
		
	if posy != sizew -1 and measure(North) != None :
		while measure(North) < measure():
			swap(North)
			return True

	if posy != 0 and measure(South) != None :
		while measure(South) > measure():
			swap(South)
			return True

	if posx != sizew -1 and measure(East) != None :
		while measure(East) < measure():
			swap(East)
			return True

	if posx != 0 and measure(West) != None :
		while measure(West) > measure():
			swap(West)
			return True
