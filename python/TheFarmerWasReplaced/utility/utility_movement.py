from utility_sensor import *

#======================================================================================================#
#	MOVEMENT TOOLS
#======================================================================================================#
#------------------------------------------------------------------------------------------------------#
#	Movement basics
#------------------------------------------------------------------------------------------------------#

def goto(tx,ty):						# goto with wrap
	
## -- Datensammlung -- ##
	x, y 	= get_x(), get_y()			# aktuelle x und y koordinaten
	size 	= get_size()				# welgrösse
	
	dxe 	= (tx -  x) % size			# distanz x-achse East
	dxw 	= ( x - tx) % size			# distanz x-achse West
	dyn 	= (ty -  y) % size			# distanz y-achse North
	dys 	= ( y - ty) % size			# distanz y-achse South
	
## -- X-Bewegung -- ##
	if dxe <= dxw :						# falls distanz x achse East kleiner als distanz x-achse West:
		for east in range(dxe):				# anzahl felder distanz x-achse East
			move(East)							# bewgen East
	else:								# andernfalls:
		for west in range(dxw):				# anzahl felder distanz x-achse West
			move(West)							# bewegen West
			
## -- Y-Bewegung -- ##
	if dyn <= dys :						# falls distanz y achse North kleiner als distanz y-achse South:
		for north in range(dyn):			# anzahl felder distanz y-achse North
			move(North)							# bewgen North
	else:								# andernfalls:
		for south in range(dys):			# anzahl felder distanz y-achse South
			move(South)							# bewegen South
#------------------------------------------------------------------------------------------------------#
def gotox(tx,ty):				# goto no wrap

	## -- y_bewegung -- ##
	if can_move(North) == True:
		while get_pos_y() < ty:
			move(North)

	## -- x_bewegung -- ##
	if can_move(East) == True:
		while get_pos_x() < tx:
			move(East)
			
	## -- y_bewegung -- ##
	if can_move(South) == True:
		while get_pos_y() > ty:
			move(South)
			
	## -- x_bewegung -- ##
	if can_move(West) == True:	
		while get_pos_x() > tx:
			move(West)
