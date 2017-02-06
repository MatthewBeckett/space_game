import globle as glo
import pygame
import entity_info as entinf 
from random import randint

from abc import ABCMeta,abstractmethod


class drawable(object):

	__metaclass__ = ABCMeta
    
	@abstractmethod	
	def draw(self,screen):
		pass

	@abstractmethod	
	def update(self):
		pass

	def remove_event_pack(self):
		pass
#
#======================================================================
#								
class logical(drawable):
	



	# image,int,int,double,double,dictionary(from entity_info) 		
	def __init__(self,image,x,y,speed_x,speed_y,info):
		self.image 		= image				
		self.x 			= x					
		self.y 			= y					
		self.speed_x 		= speed_x
		self.speed_y 		= speed_y
		self.info 		= info

		self.start_x 		= x					
		self.start_y 		= y					
		self.default_speed_x 	= speed_x
		self.default_speed_y 	= speed_y
		self.tar_speed_x 	= speed_x
		self.tar_speed_y 	= speed_y

		self.group		= info['group']
		self.width		= info['width']
		self.height		= info['height']
		self.columns		= info['columns']
		self.rows		= info['rows']
		self.column		= info['column']
		self.row		= info['row']
		self.health		= info['health']
		self.impact_damage	= info['impact_damage']
		self.controllable	= info['controllable']
		self.max_speed_x	= info['max_speed_x']
		self.max_speed_y	= info['max_speed_y']
		self.acceleration_x	= info['acceleration_x']		
		self.acceleration_y	= info['acceleration_y']
		self.deceleration_x	= info['deceleration_x']		
		self.deceleration_y	= info['deceleration_y']
		self.ai			= info['ai']
		self.remove_event	= info['remove_event']
		self.shield		= info['shield']		
		self.max_shield		= info['max_shield']
		self.shield_regen_delay = info['shield_regen_delay']
		self.level		= info['level']

		self.impact_log		= []*0
		self.shield_regen_default = self.shield_regen_delay

		# thruser/shield stuff - will try to shorten later
		self.light_thrust	= True
		self.heavy_thrust	= False
		self.shield_reload      = 0
		self.shields_up		= True		
		
		self.thrust_image	= entinf.image[24]
		self.tcolumns		= 3
		self.trows		= 2
		self.tcolumn		= 0
		self.trow		= 0
		self.tstart_row		= 0
		self.twidth		= self.thrust_image.get_rect().width/self.tcolumns
		self.theight		= self.thrust_image.get_rect().height/self.trows
		self.tanimate		= 0
		self.tanimation_delay	= 4
		self.thrusting		= True

		self.shield_image	= entinf.image[25]
		self.scolumns		= 5
		self.srows		= 4
		self.scolumn		= 0
		self.srow		= 0
		self.sstart_row		= 0
		self.swidth		= self.shield_image.get_rect().width/self.scolumns
		self.sheight		= self.shield_image.get_rect().height/self.srows
		self.sanimate		= 0
		self.sanimation_delay	= 4
		
		self.pos		= (self.x+(self.width/2),self.y+(self.height/2))
		self.rect		= pygame.Rect(self.x,self.y,self.width,self.height)
		self.border_rect	= pygame.Rect(self.x,self.y,self.width,self.height)


		glo.ID +=1
		self.id			= glo.ID 

		self.firing 		= False
		self.reloading 		= 0

		self.remove		= False
		
		self.screen_width 	= glo.screen_width		
		self.screen_height 	= glo.screen_height
		self.max_right		= glo.max_right
		self.max_left		= glo.max_left
		self.max_up		= glo.max_up
		self.max_down		= glo.max_down

		self.hostile		= False

		self.count_lmt 		= randint(0,10)
		self.count 		= 0
		self.panic_time 	= 0

		if self.group == "npc":
			self.row = randint(0,self.rows) 


	def update(self):




		""" not too fast """		
		# keeping within objects max speed
		if self.tar_speed_x < -self.max_speed_x < 0:
			self.tar_speed_x = -self.max_speed_x
		elif self.tar_speed_x < self.max_speed_x < 0:
			self.tar_speed_x = self.max_speed_x
		if self.tar_speed_y < -self.max_speed_y < 0:
			self.tar_speed_y = -self.max_speed_y
		elif self.tar_speed_y < self.max_speed_y < 0:
			self.tar_speed_y = self.max_speed_y
		


		if self.controllable:

			# update player pos
			glo.player_pos_x = self.pos[0]
			glo.player_pos_y = self.pos[1]
			glo.player_id	 = self.id

			
			glo.health		= self.health
			glo.shield		= self.shield
			
			# player movement
			if 	glo.pressing_up:
				self.tar_speed_y = -self.max_speed_y			
			
			elif 	glo.pressing_down:				
				self.tar_speed_y = self.max_speed_y
			
			elif	glo.pressing_up == False and glo.pressing_down == False:			
				self.tar_speed_y = 0
			
			if 	glo.pressing_left:
				self.tar_speed_x = -self.max_speed_x

			elif 	glo.pressing_right:
				self.tar_speed_x = self.max_speed_x

			else:
				self.tar_speed_x = 0

			if glo.pressing_shift:
				self.speed_y *= 0.65
				self.speed_x *= 0.65

			elif glo.pressing_z and self.speed_x > 0:
				self.max_speed_x = 80
			
			else:
				self.max_speed_x = self.info['max_speed_x']
			
			
			# player firing weapon
			if	glo.pressing_space:
				self.firing = True
	
			else:
				self.firing = False


								


		""" speed, acceleration, deceleration """
		# X axis
		if self.tar_speed_x == 0 and 0 < self.speed_x:
			self.speed_x -=self.deceleration_x
			self.thrusting = True
			self.heavy_thrust = False
			self.light_thrust = True
		elif self.tar_speed_x < self.speed_x:
			self.speed_x -=self.acceleration_x
			self.thrusting = False
			self.heavy_thrust = False
			self.light_thrust = False
		if self.tar_speed_x == 0 and 0 > self.speed_x:
			self.speed_x +=self.deceleration_x
			self.thrusting = True
			self.heavy_thrust = False
			self.light_thrust = True
		elif self.tar_speed_x > self.speed_x:
			self.speed_x +=self.acceleration_x
			self.thrusting = True
			self.heavy_thrust = True
			self.light_thrust = False


		# Y axis
		if self.tar_speed_y == 0 and 0 < self.speed_y:
			self.speed_y -=	self.deceleration_y
		elif self.tar_speed_y < self.speed_y:
			self.speed_y -= self.acceleration_y
		if self.tar_speed_y == 0 and 0 > self.speed_y:
			self.speed_y += self.deceleration_y
		elif self.tar_speed_y > self.speed_y:
			self.speed_y += self.acceleration_y


		# stop X/Y axis drifting
		if -1 < self.speed_y < 1:
			self.speed_y = 0 
		if -1 < self.speed_x < 1:
			self.speed_x = 0 

		# update globle speed
		if self.controllable: 
			if self.x >= self.max_right: 
				self.x = self.max_right
				glo.player_speed_x = self.speed_x
			
			elif self.x <= self.max_left: 
				self.x = self.max_left
				glo.player_speed_x = self.speed_x
			else:
				glo.player_speed_x = 0
 
			if self.y <= self.max_up: 
				self.y = self.max_up

			elif self.y >= self.max_down: 
				self.y = self.max_down
			
				
		# location from speed
			if glo.pressing_ctrl:
				glo.player_speed_x = self.speed_x
			
			else:
				self.x += self.speed_x

			
		else:
			self.x += self.speed_x-glo.player_speed_x

		self.y += self.speed_y

		# update pos
		self.pos = (self.x+(self.width/2),self.y+(self.height/2))			
		self.tar_speed_x = self.default_speed_x

		if self.ai:
			# update border pygame.Rect
			self.border_ratio = self.info['border_ratio']
			self.border_rect = pygame.Rect(self.x - ((self.width/2)*self.border_ratio) ,
						self.y-((self.height/2)*self.border_ratio),
						(self.width*8)*self.border_ratio,
						self.height+(self.height*self.border_ratio)
						)
			
			if glo.wanted_level > 0 and self.group == 'police':
				self.hostile = True

			if self.hostile == False:
				self.firing = False
				self.tar_speed_y = 0
				
			if self.hostile:		
				print self.group+' '+str(self.id)+' hostile'		
				if self.pos[1] < glo.player_pos_y-8 and self.panic_time <= 0:
					self.tar_speed_y = 3
					self.firing = False
				elif self.pos[1] > glo.player_pos_y+8 and self.panic_time <= 0:
					self.tar_speed_y = -3
					self.firing = False
				else:
					if self.panic_time <= 0:
						self.firing = True
						self.tar_speed_y = 0
	
				if self.pos[0] < glo.player_pos_x - 128:
					self.tar_speed_x = self.max_speed_x
			
				elif self.pos[0] > glo.player_pos_x - 32:
					if self.group == 'police':
						self.panic_time = 40
						self.tar_speed_x = -4
					else:
						self.tar_speed_x = self.max_speed_x
						self.panic_time = 40
						self.firing = False
				else:				
					self.tar_speed_x = self.default_speed_x	
	

				if self.count > self.count_lmt:
					if self.panic_time > 0:
						glo.wanted +=1
						self.tar_speed_y = randint(-3,3)
					else:
						self.speed_x = self.default_speed_x
						self.panic_time = 0
					self.count_lmt = randint(16,128)
					self.count = 0
				self.count+=1
				self.panic_time -=1

			if glo.player_alive == False:
				self.hostile == False
				self.firing == False
			


		# update physical pygame.Rectangle 		
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

		if self.shield > self.max_shield*0.8:
			self.srows 	= 1
			self.sstart_row	= 0			
		elif self.shield > self.max_shield*0.6:
			self.srows 	= 2	
			self.sstart_row	= 1		
		elif self.shield > self.max_shield*0.4:
			self.srows 	= 3	
			self.sstart_row	= 2		
		elif self.shield > self.max_shield*0.2:
			self.srows 	= 4			
			self.sstart_row	= 3
			

		if self.shield_regen_delay < 0:
			self.shield_regen_delay = self.shield_regen_default
			if self.shield < self.max_shield:
				self.shield +=1
		self.shield_regen_delay -=1


		if self.heavy_thrust:
			self.tstart_row = 1
			self.trows = 2

		elif self.light_thrust:
			self.tstart_row = 0
			self.trows = 1

		if self.shield_reload > 0:
			self.shield_reload -=1

		""" animation """
		self.tanimate -= 1				
		if self.tanimate <= 0:
			self.tanimate = self.tanimation_delay
			self.tcolumn +=1
			if self.tcolumn > self.tcolumns-1:
				self.tcolumn = 0
				self.trow +=1
				if self.trow > self.trows-1:
					self.trow = self.tstart_row

		""" animation """
		self.sanimate -= 1				
		if self.sanimate <= 0:
			self.sanimate = self.sanimation_delay
			self.scolumn +=1
			if self.scolumn > self.scolumns-1:
				self.scolumn = 0
				self.srow +=1
				if self.srow > self.srows-1:
					self.srow = self.sstart_row





		""" firing weapons """
		if self.info['weapon'] > 0:
			if self.info['weapon'] == 1:
				if self.firing:
					if self.reloading > glo.fire_rate_0:
						glo.missile_0.append(
							(
								self.x+self.width+self.speed_x+16,
								self.y+self.info['weapon_1_height']+self.speed_y,
								self.id 
							))
						self.reloading = 0
				
				if self.reloading < glo.fire_rate_0+1:
					self.reloading +=1
		


		""" removing """
		if self.x > self.screen_width+1100 or self.x < -300 or self.y > self.screen_height+500 or self.y < -500 or self.health < 0: 
				self.remove = True		
			
			

	def draw(self,screen):

		screen.blit(	self.image,
				(self.pos[0]-(self.width/2),self.pos[1]-(self.height/2)),
				(self.width*self.column,self.height*self.row,self.width,self.height)
				)

		if self.thrusting:
			screen.blit(	self.thrust_image,
					(self.x-self.twidth,self.pos[1]-(self.theight/2)),
					(self.twidth*self.tcolumn,self.theight*self.trow,self.twidth,self.theight)
					)

		if self.shield_reload > 0:
			screen.blit(	self.shield_image,
					(self.pos[0]-(self.swidth/2),self.pos[1]-(self.sheight/2)),
					(self.swidth*self.scolumn,self.sheight*self.srow,self.swidth,self.sheight)
					)


	def take_damage(self,imp,ID,group):
		if imp > self.shield:
			imp -= self.shield
			self.shield = 0
			self.health -= imp
			self.shield_reload = 8
		else:
			self.shield -= imp
			self.shield_reload = (imp * 1.5)

		if ID == glo.player_id:# and group == 'missile':
			glo.text.append((imp/10,(0,255,0),self.pos,30))
			self.hostile = True
			glo.xp += imp/10
			glo.wanted += (10*self.level)


	def remove_event_pack(self):		
		return (self.remove_event,self.pos[0],self.pos[1],self.speed_x,self.speed_y,self.level)


#
#======================================================================
#								
class animated_solid(drawable):
	def __init__(self,image,x,y,speed_x,speed_y,info):
		self.image 		= image				
		self.x 			= x					
		self.y 			= y
		self.speed_x 		= speed_x
		self.speed_y 		= speed_y
		self.info 		= info

		self.group		= info['group']		
		self.health		= info['health']
		self.width		= info['width']
		self.height		= info['height']
		self.column		= info['column']
		self.row		= info['row']
		self.columns		= info['columns']
		self.rows		= info['rows']
		self.remove_event  	= info['remove_event']
		self.impact_damage	= info['impact_damage']
		self.animation_delay	= info['animation_delay']
		self.animate		= 0
		

		self.level		= info['level']
		self.rect 		= pygame.Rect(self.x,self.y,self.width,self.height)
		self.start_x 		= x					
		self.start_y 		= y					
		self.remove 		= False
		self.screen_width 	= glo.screen_width		
		self.screen_height 	= glo.screen_height
		self.pos 		= (self.x+(self.info['width']/2),self.y+(self.info['height']/2))
		glo.ID +=1
		self.id			= glo.ID
		self.impact_log		= []*0

	def update(self):

		""" animation """
		self.animate -= 1				
		if self.animate <= 0:
			self.animate = self.animation_delay
			self.column +=1
			if self.column > self.info['columns']-1:
				self.column = 0
				self.row +=1
				if self.row > self.rows-1:
					self.row = 0


		# update physical pygame.Rectangle 		
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)


		# update pos
		self.pos = (self.x+(self.info['width']/2),self.y+(self.info['height']/2))

		# location from speed
		self.x += self.speed_x-glo.player_speed_x
		self.y += self.speed_y


						
		""" removing """
		if self.x > self.screen_width+1100 or self.x < -300 or self.y > self.screen_height+500 or self.y < -500 or self.health < 0: 
				self.remove = True		


	def draw(self,screen):
		screen.blit(	self.image,
				(self.pos[0]-(self.width/2),self.pos[1]-(self.height/2)),
				(self.width*self.column,self.height*self.row,self.width,self.height)
				)

	def take_damage(self,imp,ID,group):
		self.health -= imp
		if ID == glo.player_id and group == 'missile':
			glo.text.append((imp/10,(0,255,0),self.pos,30))
			glo.xp += imp/10
			glo.wanted += (10*self.level)
		


	def remove_event_pack(self):
		return (self.remove_event,self.pos[0],self.pos[1],self.speed_x,self.speed_y,self.level)

#
#======================================================================
#								
class simple_solid(drawable):
	def __init__(self,image,x,y,speed_x,speed_y,info,ID):
		self.image 		= image				
		self.x 			= x					
		self.y 			= y
		self.speed_x 		= speed_x
		self.speed_y 		= speed_y
		self.info 		= info

		self.group		= info['group']
		self.health		= info['health']
		self.remove_event	= info['remove_event']					
		self.column		= info['column']		
		self.row		= info['row']			
		self.width		= info['width']			
		self.height		= info['height']		
		self.impact_damage	= info['impact_damage']			
		self.level		= info['level']

		self.rect		= pygame.Rect(self.x,self.y,self.width,self.height)
		self.start_x 		= x					
		self.start_y 		= y	
		
		if info['rotating']:
			self.rotate		= randint(0,359)
			self.rotate_speed	= (self.speed_x - self.speed_y)*.5
		else:
			self.rotate		= 0
			self.rotate_speed	= 0
			
		self.remove		= False				
		self.screen_width 	= glo.screen_width		
		self.screen_height 	= glo.screen_height

		self.id			= ID

		# update pos
		self.pos = (self.x+(self.width/2),self.y+(self.height/2))

		if self.group == 'roid'  or self.group == 'pickup':
			self.column = randint(0,3)


		


	def update(self):
		self.rotate += self.rotate_speed


		# update physical pygame.Rectangle 		
#		self.rect = pygame.Rect(self.x+self.speed_x,self.y+self.speed_y,self.width,self.height)

		# location from speed
		self.x += self.speed_x-glo.player_speed_x
		self.y += self.speed_y

		# update pos
		self.pos = (self.x+(self.width/2),self.y+(self.height/2))

		if self.x > self.screen_width + 1000 or	self.x < -500 or self.y > self.screen_height + 200 or self.y < -200 or self.health < 0:
			self.remove = True


	def draw(self,screen):

		#rotation
		suf = pygame.Surface((self.width,self.height))
		suf.set_colorkey((0,0,0))
		pygame.Surface.convert_alpha(suf)
		#suf.set_alpha(128)
		
		suf.blit(	self.image,
				(0,0),
				(self.width*self.column,self.height*self.row,self.width,self.height)
				)

		
		
		img = pygame.Surface.convert(suf)
		img = pygame.transform.rotate(img,self.rotate)
		w=img.get_rect().width
		h=img.get_rect().height
		

		# draw to screen
		screen.blit(img,(self.x-(w/2),self.y-(h/2)))

		# update physical pygame.Rectangle 		
		self.rect = pygame.Rect(self.x-(w/2),self.y-(h/2),w,h)


	def take_damage(self,imp,ID,group):
		self.health -= imp
		if ID == glo.player_id and group == 'missile':
			glo.xp += imp/10
			glo.text.append((imp/10,(0,255,0),self.pos,30))

		if self.group == 'pickup' and group == 'player':
			points = randint(10*(self.column+1),11*(self.column+1))
			glo.credit += points 
			glo.text.append((points,(255,0,0),self.pos,80))




	def remove_event_pack(self):	
		return (self.remove_event,self.pos[0],self.pos[1],self.speed_x,self.speed_y)
		
#
#======================================================================
#								
class animated_ghost(drawable):
	def __init__(self,image,x,y,speed_x,speed_y,info):
		self.image 		= image				
		self.x 			= x - (info['width']/2)					
		self.y 			= y - (info['height']/2)
		self.speed_x 		= speed_x
		self.speed_y 		= speed_y
		self.info 		= info

		self.group		= info['group']
		self.width		= info['width']
		self.height		= info['height']
		self.column		= info['column']
		self.row		= info['row']
		self.columns		= info['columns']
		self.rows		= info['rows']
		self.animation_delay	= info['animation_delay']

		self.animate		= 0
		self.start_x 		= self.x					
		self.start_y 		= self.y

		self.remove		= False
		self.rotate		= randint(0,355)	
		
	def update(self):	

		""" animation """
		self.animate -= 1				
		if self.animate <= 0:
			self.animate = self.animation_delay
			self.column +=1
			if self.column > self.columns-1 :
				self.column = 0
				self.row +=1
				if self.row > self.rows-1:
					if self.group == 'explosion':
						self.remove = True
					self.row = 0

		# location from speed
		self.x += self.speed_x
		self.y += self.speed_y


	def draw(self,screen):
		#rotation
		suf = pygame.Surface((self.width,self.height))
		suf.set_colorkey((0,0,0))
		pygame.Surface.convert_alpha(suf)
		#suf.set_alpha(128)
		
		suf.blit(	self.image,
				(0,0),
				(self.width*self.column,self.height*self.row,self.width,self.height)
				)

		
		
		img = pygame.Surface.convert(suf)
		center = img.get_rect().center		
		img = pygame.transform.rotate(img,self.rotate)
		w=img.get_rect().width
		h=img.get_rect().height
		

		# draw to screen
		screen.blit(img,(self.x-(w/2),self.y-(h/2)))

	def remove_event_pack(self):
		return (self.remove_event,0)
#
#======================================================================
#								
class simple_ghost(drawable):
	def __init__(self,image,x,y,speed_x,speed_y,info):
		self.image 		= image				
		self.x 			= x					
		self.y 			= y
		self.speed_x 		= speed_x
		self.speed_y 		= speed_y
		self.info 		= info

		self.group		= info['group']
		self.width		= info['width']
		self.height		= info['height']
		self.column		= info['column']
		self.row		= info['row']

		self.start_x 		= x					
		self.start_y 		= y					

		self.remove		= False

	def update(self):	

		if self.group == 'scenery':
			# looping scenery by placing image at the end of a que 
			# after it has traveled it's width past 0.
			if self.x <= 0-self.width:
				self.x = self.width * glo.background_0-1

		# location from speed
		self.x += self.speed_x-glo.player_speed_x
		self.y += self.speed_y

	
	def draw(self,screen):
		screen.blit(	self.image,
				(self.x,self.y),
				(self.width*self.column,self.height*self.row,self.width,self.height)
				)
						


	def remove_event_pack(self):
		return (self.remove_event,0)

