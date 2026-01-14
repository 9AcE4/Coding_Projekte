from utility_sensor import *
from utility_movement import *
from utility_plant import *

set_world_size(16)

# - - - - - - - - - - - - - - - - - - - - - - - - - - # DEF tile_scan()
def tile_scan():
	
	x = get_x()
	y = get_y()
	
	N = can_move(North)
	E = can_move(East)
	S = can_move(South)
	W = can_move(West)
	
	maze[(x,y)] = {
			"N" : N,
			"E" : E,
			"S" : S,
			"W" : W
	}
	
## -- ausgleich gegenseite -- ##
	if phase_hunt == True:
	# - norden - #
		if (x,y+1) in maze:
			maze[(x,y+1)]["S"] = N
	# - osten - #
		if (x+1,y) in maze:
			maze[(x+1,y)]["W"] = E
	# - süden - #
		if (x,y-1) in maze:
			maze[(x,y-1)]["N"] = S
	# - westen - #
		if (x-1,y) in maze:
			maze[(x-1,y)]["E"] = W
	#print((x,y),maze[(x,y)])
# - - - - - - - - - - - - - - - - - - - - - - - - - - # DEF A*
def find_path_astar(start, goal):
	open_list   = [start]
	came_from   = {}
	g_score     = {}
	f_score     = {}
	closed      = {}          # schon „fertig“ bearbeitete Knoten

	g_score[start] = 0

	# Manhattan + 25% (int, ohne floats)
	h0 = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
	h0 = h0 + (h0 // 4)
	f_score[start] = h0

	while len(open_list) > 0:

		# --- bestes f auswählen (ohne lambda) ---
		current = open_list[0]
		i = 1
		while i < len(open_list):
			node = open_list[i]
			fv = 999999
			if node in f_score:
				fv = f_score[node]
			cv = 999999
			if current in f_score:
				cv = f_score[current]
			if fv < cv:
				current = node
			i += 1

		# Ziel?
		if current == goal:
			# Pfad rekonstruieren, ohne reverse()
			path = []
			p = current
			while p in came_from:
				path.append(p)
				p = came_from[p]
			path.append(start)
			final_path = []
			k = len(path) - 1
			while k >= 0:
				final_path.append(path[k])
				k -= 1
			return final_path

		# current aus open entfernen
		i = 0
		while i < len(open_list):
			if open_list[i] == current:
				open_list.pop(i)
				break
			i += 1

		# current schließen
		closed[current] = True

		# --- Nachbarn in Zielrichtung priorisiert ---
		cx = current[0]
		cy = current[1]
		ordered = []
		# grob Richtung Ziel zuerst
		if goal[1] > cy: 
			ordered.append("N")
		if goal[0] > cx: 
			ordered.append("E")
		if goal[1] < cy: 
			ordered.append("S")
		if goal[0] < cx: 
			ordered.append("W")
		# fehlende Richtungen ergänzen
		base = ["N","E","S","W"]
		j = 0
		while j < 4:
			d = base[j]
			present = False
			k = 0
			while k < len(ordered):
				if ordered[k] == d:
					present = True
					break
				k += 1
			if present == False:
				ordered.append(d)
			j += 1

		# --- Nachbarn verarbeiten ---
		d = 0
		while d < 4:
			dir = ordered[d]
			d += 1

			if maze[current][dir] == False:
				continue

			if dir == "N":
				nb = (cx, cy+1)
			elif dir == "E":
				nb = (cx+1, cy)
			elif dir == "S":
				nb = (cx, cy-1)
			else:
				nb = (cx-1, cy)

			# schon abgeschlossen und nicht besser? -> skip
			if nb in closed:
				# wenn geschlossen, nur weiter falls wir tatsächlich bessere Kosten hätten
				oldc = 999999
				if nb in g_score:
					oldc = g_score[nb]
				if oldc <= g_score[current] + 1:
					continue

			# g neu
			g_here = 999999
			if current in g_score:
				g_here = g_score[current]
			tentative = g_here + 1

			old = 999999
			if nb in g_score:
				old = g_score[nb]

			if tentative < old:
				came_from[nb]  = current
				g_score[nb]    = tentative
				hv = abs(nb[0] - goal[0]) + abs(nb[1] - goal[1])
				hv = hv + (hv // 4)  # leicht übergewichtet
				f_score[nb]    = tentative + hv

				# nur anhängen, wenn noch nicht in open_list
				present = False
				k = 0
				while k < len(open_list):
					if open_list[k] == nb:
						present = True
						break
					k += 1
				if present == False:
					open_list.append(nb)

	return None

# - - - - - - - - - - - - - - - - - - - - - - - - - - # START
#while num_items(Items.Gold) < 616448:
while True:
# - - - - - - - - - - - - - - - - - - - - - - - - - - # Maze Initialisieren
	clear()
	#change_hat(Hats.Wizard_Hat)				# drone test
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,( get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes)) -1 ))
# - - - - - - - - - - - - - - - - - - - - - - - - - - # direction swaps
	directions = [North, East, South, West]
	index = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - - # phase START
	phase_scan = True
	phase_hunt = False
# - - - - - - - - - - - - - - - - - - - - - - - - - - # maze dic
	maze = {}
# - - - - - - - - - - - - - - - - - - - - - - - - - - # gesamtes feld scannen
	while phase_scan == True:
		
		#print(get_x(),get_y(),"|",len(maze))
			
		if len(maze) == get_world_size()*get_world_size():	# Phase STOP
			phase_scan = False
			phase_hunt = True
			
		turn_right = (index + 1) % 4
		if move(directions[turn_right]):
			tile_scan()
			index = turn_right
			continue
					
		if move(directions[index]):
			tile_scan()
			continue
			
		turn_left = (index - 1) % 4
		if move(directions[turn_left]):
			tile_scan()
			index = turn_left
			continue
			
		turn_back = (index + 2) % 4
		index = turn_back
		move(directions[index])
		tile_scan()
# - - - - - - - - - - - - - - - - - - - - - - - - - - #
	while phase_hunt == True:
		for repeats in range(301):
		
			sx,sy = get_x(), get_y()
			tx,ty = measure()
			
			path = find_path_astar((sx,sy),(tx,ty))
			#print(path)
			
			if path != None:
				i = 1 
				while i < len(path):
					goto(path[i][0],path[i][1])
					tile_scan()
					i += 1
			else:
				print("No way!")
				
			
			if get_entity_type() == Entities.Treasure:
				use_item(Items.Weird_Substance,( get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes)) -1 ))
				quick_print(repeats)
			
		if get_entity_type() == Entities.Treasure:	
			harv()
			phase_scan = True
			phase_hunt = False
