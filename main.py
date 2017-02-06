import entity
import globle as glo
import pygame as py
import entity_info as info
import itertools
from random import randint
import time
from hud import hud
from text import text

#######################		FUNCTIONS	 ##############################


def randomize_spawn_rate(t):
	t -=1
	if t <= 0:
		t = randint(50,10000)	
		glo.npc_spawn_rate	= randint(1,15000)
		glo.roid_spawn_rate	= randint(1,15000)
		glo.trader_spawn_rate	= randint(1,100)

def wanted_level():
	if glo.wanted > 16000:
		glo.wanted_level = 5
		glo.police_spawn_rate = 10000
	elif glo.wanted > 8000:
		glo.wanted_level = 4
		glo.police_spawn_rate = 4000
	elif glo.wanted > 4000:
		glo.wanted_level = 3
		glo.police_spawn_rate = 2000
	elif glo.wanted > 2000:
		glo.wanted_level = 2
		glo.police_spawn_rate = 1000
	elif glo.wanted > 1000:
		glo.wanted_level = 1
		glo.police_spawn_rate = 500
	elif glo.wanted <= 1000:
		glo.wanted_level = 0

def append_text():
	t = 0
	while t < len(glo.text):
		texts.append(
			text(	glo.text[t][0],
				glo.text[t][1],
				glo.text[t][2],
				glo.text[t][3]
				)
			)
		del glo.text[t]
		t+=1


def append_missile():
	m = 0
	while m < len(glo.missile_0):
		solid_objects.append(
			ent.simple_solid(
				info.image[info.missile_0['image']],
				glo.missile_0[m][0],
				glo.missile_0[m][1],
				16,
				0,
				info.missile_0,
				glo.missile_0[m][2]
			))
		del glo.missile_0[m]
		m+=1


def avoid():

	for a in solid_objects:
			for b in solid_objects:
				if a != b and a.group == 'npc' or a.group == 'police':
 					if a.border_rect.colliderect(b.rect): 
						if a.pos[1] > b.pos[1]:
							a.tar_speed_y = a.max_speed_y
						elif a.pos[1] < b.pos[1]:
							a.tar_speed_y = -a.max_speed_y

						if a.pos[0] < b.pos[0]:
							a.tar_speed_x = (a.default_speed_x -3)
						elif a.pos[0] > b.pos[0]:
							a.tar_speed_x = a.max_speed_x 
						
						if a.group == 'police' and b.group == 'missile' and b.id == glo.ID:
							a.hostile = True
				

def collisio():
	for a in solid_objects:
		for b in solid_objects:
			if a != b:
				if a.rect.colliderect(b.rect):
					a.take_damage(b.impact_damage,b.id,b.group)
					b.take_damage(a.impact_damage,a.id,a.group)
					a.x -a.speed_x
					a.y -a.speed_y			
					b.x -b.speed_x
					b.y -b.speed_y					
					if a.id == glo.player_id:
						running =False					
					#	glo.xp +=b.info['xp']
					#	b.impact_log.append(glo.ID)
					#	glo.wanted += b.info['xp']
					if a.group == 'player' and b.group == 'trader' and pressing_t:
						pause = True


def collision():
	a = 0
	t = len(solid_objects)
	while a < t:
		if a < t:
			b = a+1
		while b < t:
			if solid_objects[a].rect.colliderect(solid_objects[b].rect):
				solid_objects[a].take_damage(solid_objects[b].impact_damage,solid_objects[b].id,solid_objects[b].group)
				solid_objects[b].take_damage(solid_objects[a].impact_damage,solid_objects[a].id,solid_objects[a].group)
				solid_objects[a].x -solid_objects[a].speed_x
				solid_objects[a].y -solid_objects[a].speed_y			
				solid_objects[b].x -solid_objects[b].speed_x
				solid_objects[b].y -solid_objects[b].speed_y					
				if solid_objects[a].id == glo.player_id:
					pass		
				#	glo.wanted += b.info['xp']
			b+=1
		a+=1
		


def debug():
	print '::::::::::::::::::::'
	print 'solid objects : '+str(len(solid_objects))
	print 'ghost objects : '+str(len(ghost_objects))
	print 'police        : '+str(police)

def remove_event(event):
	if event[0] == 0:
		pass
	elif event[0] == 1:
		ghost_objects.append(
				ent.animated_ghost(
					info.image[info.impact_0['image']],
					event[1],
					event[2],
					0,
					0,
					info.impact_0))
	elif event[0] == 2:
		ghost_objects.append(
				ent.animated_ghost(
					info.image[info.explosion_0['image']],
					event[1],
					event[2],
					0,
					0,
					info.explosion_0))
	elif event[0] == 3:
		ghost_objects.append(
				ent.animated_ghost(
					info.image[info.roid_explode['image']],
					event[1],
					event[2],
					0,
					0,
					info.roid_explode))
	
	elif event[0] == 4:
		r = randint(2,3)
		for x in range(0,r):
			xl = randint(int(event[1]-32),int(event[1]+32))
			yl = randint(int(event[2]-32),int(event[2]+32))		
			xs = -(event[1] - xl)*0.1
			ys = -(event[2] - yl)*0.1

			solid_objects.append(
				ent.simple_solid(
					info.image[info.roid_0['image']],
					xl,
					yl,
					xs,
					ys,
					info.roid_0,
					glo.ID))					
			glo.ID +=1		
	
	elif event[0] == 5:
		r = randint(2,3)
		for x in range(0,r):
			xl = randint(int(event[1]-32),int(event[1]+32))
			yl = randint(int(event[2]-32),int(event[2]+32))		
			xs = -((event[1] - xl)*0.1)
			ys = -(event[2] - yl)*0.1

			solid_objects.append(
				ent.simple_solid(
					info.image[info.roid_1['image']],
					xl,
					yl,
					xs,
					ys,
					info.roid_1,
					glo.ID))					
			glo.ID +=1	
	
	elif event[0] == 7:
		ghost_objects.append(
				ent.animated_ghost(
					info.image[info.explosion_0['image']],
					event[1],
					event[2],
					0,
					0,
					info.explosion_0))
		for x in range(0,event[5]):
			solid_objects.append(
				ent.simple_solid(
					info.image[info.pickup['image']],
					event[1],
					event[2],
					randint(-2,1),
					randint(-1,1),
					info.pickup,
					glo.ID,))
			glo.ID +=1


def lines():
	
	#warp_count +=1
	for x in range(0,len(points_x)):
		py.draw.line(screen,(255,255,255),(points_x[x],points_y[x]),(points_x[x]-(glo.player_speed_x*.5),points_y[x]),1)
	#else:
	#	while warp_count > 0:
	#		warp_count -=1
			
			
###############################################################################



""" pygame window """
py.init()
screen = py.display.set_mode((glo.screen_width,glo.screen_height))
py.display.set_caption(glo.window_caption)


""" fps clock """
clock = py.time.Clock()


""" class initializing """
ent = entity

""" loop control """
running = True

HUD = hud()
paused = False


police = 0

time_2_randomize = 0

""" lists """
background_0 	= []*0
solid_objects 	= []*0
ghost_objects	= []*0
ship_layers	= []*0
points_x 	= []*0
points_y	= []*0
texts		= []*0


total = randint(10,500)

for x in range(0,total):
	points_x.append(randint(0,glo.screen_width + 2000))
	points_y.append(randint(0,glo.screen_height))
	

""" pre-loop objects """

solid_objects.append( 
	ent.logical(
		info.image[info.player['image']],	# image
		200,					# x
		glo.screen_height /2,			# y
		0,					# speed x
		0,					# speed y
		info.player				# entity info
	))



""" loop start """
while running:


	""" events """
	for evt in py.event.get():
		if evt.type == py.QUIT:
			running = False
       
		""" keyboad events """
		if evt.type == py.KEYDOWN:
			if evt.key == py.K_ESCAPE:
				if paused:
					paused = False
				else:
					paused = True

			if evt.key == py.K_i:
				if paused:
					paused = False
				else:
					paused = True

			if evt.key == py.K_UP:
				glo.pressing_up = True  
			elif evt.key == py.K_DOWN:
				glo.pressing_down = True
			if evt.key == py.K_LEFT:
				glo.pressing_left = True  
			elif evt.key == py.K_RIGHT:
				glo.pressing_right = True 
			if evt.key == py.K_SPACE:
				glo.pressing_space = True
			if evt.key == py.K_LCTRL:
				glo.pressing_ctrl = True
			if evt.key == py.K_LSHIFT:
				glo.pressing_shift = True
			if evt.key == py.K_z:
				glo.pressing_z = True
			if evt.key == py.K_t:
				glo.pressing_t = True
			if evt.key == py.K_r:
				p = False
				for o in solid_objects:
					if o.group == 'player':
						p = True
						break;
				if p == False:
					solid_objects.append( 
								ent.logical(
								info.image[info.player['image']],	# image
								200,					# x
								glo.screen_height /2,			# y
								0,					# speed x
								0,					# speed y
								info.player				# entity info
							))
					


	        elif evt.type == py.KEYUP:
			if evt.key == py.K_UP:
				glo.pressing_up = False 
			if evt.key == py.K_DOWN:
				glo.pressing_down = False 
	                if evt.key == py.K_LEFT: 
				glo.pressing_left = False 
			if evt.key == py.K_RIGHT:
				glo.pressing_right = False 
			if evt.key == py.K_SPACE:
				glo.pressing_space = False
			if evt.key == py.K_LCTRL:
				glo.pressing_ctrl = False
			if evt.key == py.K_LSHIFT:
				glo.pressing_shift = False
			if evt.key == py.K_z:
				glo.pressing_z = False
			if evt.key == py.K_t:
				glo.pressing_t = False


	if not paused:
		
		randomize_spawn_rate(time_2_randomize)


		millis = int(round(time.time() * 1000))
	
		
		# add random objects 
		if randint(0,72000 / glo.npc_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.logical(
					info.image[info.npc_0['image']],			# image
					randint(-glo.screen_width,-100),			# x
					randint(0,glo.screen_height),				# y
					randint(-2,4),						# speed x
					0,							# speed y
					info.npc_0						# entity info
				))

		if randint(0,72000 / glo.npc_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.logical(
					info.image[info.npc_1['image']],			# image
					randint(100+glo.screen_width,glo.screen_width+1000),	# x
					randint(0,glo.screen_height),				# y
					randint(-2,4),						# speed x
					0,							# speed y
					info.npc_1						# entity info
				))

		if randint(0,72000 / glo.trader_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.animated_solid(
					info.image[info.trader['image']],			
					randint(glo.screen_width+info.trader['width'],glo.screen_width+info.trader['width']+1000),	
					randint(0+info.trader['height'],glo.screen_height-info.trader['height']),	
					randint(1,2),						
					0,							
					info.trader						
				))
	
		if randint(0,22000 / glo.trader_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.animated_solid(
					info.image[info.trader['image']],			
					randint(-glo.screen_width+info.trader['width'],-info.trader['width']),	
					randint(0+info.trader['height'],glo.screen_height-info.trader['height']),	
					randint(1,2),						
					0,							
					info.trader						
				))
	
		if randint(0,72000 / glo.roid_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.simple_solid(
					info.image[info.roid_2['image']],			# image
					randint(100+glo.screen_width,glo.screen_width+2000),	# x
					randint(0,glo.screen_height),				# y
					randint(-2,1),						# speed x
					randint(-1,1),						# speed y
					info.roid_2,						# entity info
					glo.ID								# entity info
				))
			glo.ID +=1
	
		if randint(0,72000 / glo.roid_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.simple_solid(
					info.image[info.roid_1['image']],			# image
					randint(100+glo.screen_width,glo.screen_width+2000),	# x
					randint(0,glo.screen_height),				# y
					randint(-2,1),						# speed x
					randint(-1,1),						# speed y
					info.roid_1,						# entity info
					glo.ID			
				))
			glo.ID +=1
	
		if randint(0,72000 / glo.police_spawn_rate) == 1 and glo.max_entities > len(solid_objects):
			solid_objects.append( 
				ent.logical(
					info.image[info.police_0['image']],			# image
					randint(100+glo.screen_width,glo.screen_width+2000),	# x
					randint(0,glo.screen_height),				# y
					randint(-3,3),						# speed x
					0,							# speed y
					info.police_0,						# entity info
					#glo.ID							# entity info
				))
			glo.ID +=1
	
		# update stars			
		for i in range(0,len(points_x)):
			points_x[i]-=1
			if points_x[i] < -100 :
				points_x[i]+=glo.screen_width + 2000
	
		collision()


		""" update """	
		append_missile()
		append_text()
		avoid()
	
		for b in background_0:
			b.update()

		p = 0
		for obj in solid_objects:
			obj.update()	
			if obj.group == 'police':
				p +=1
		police = p

		for g in ghost_objects:
			g.update()

		for b in background_0:
			b.update()

		for txt in texts:
			txt.update()				



		i = 0
		while i < len(solid_objects):
			solid_objects[i].update()
			if solid_objects[i].remove:
				if solid_objects[i].group == 'player':
					glo.ID = 0
					glo.player_alive = False
			
				print solid_objects[i].remove
				remove_event(solid_objects[i].remove_event_pack())		
				del solid_objects[i]
			i +=1
		i = 0	
		while i < len(ghost_objects):
			ghost_objects[i].update()
			if ghost_objects[i].remove:
				print ghost_objects[i].remove
				del ghost_objects[i]
			i +=1	
		i=0
		while i < len(texts):
			texts[i].update()
			if texts[i].remove:
				print texts[i].remove
				del texts[i]
			i +=1	
		wanted_level()
	
		HUD.update()	
		py.display.update()

	""" draw """
	screen.fill((0,10,10))
	lines()

	for o in solid_objects:
		o.draw(screen)
	for g in ghost_objects:
		g.draw(screen)
	HUD.draw(screen)


	for t in texts:
		t.draw(screen)
	
	""" count frame """
	glo.frame_count +=1

	debug()
	print 'compute time = '+str(int(round(time.time() * 1000)) - millis)


	""" fps """
	clock.tick(glo.fps)

py.quit()








