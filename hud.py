import globle as glo
from pygame import font

class hud:

	
	def __init__(self):
		self.font 		= font.SysFont("DejaVu Sans",15)
		self.health 		= "health: "+str(glo.health)
		self.shield 		= "shield: "+str(glo.shield)
		self.wanted_level 	= "wanted: "+str(glo.wanted_level)
		self.credit 		= "credit: "+str(glo.credit)
		self.credit 		= "xp: "+str(glo.xp)	
		self.xp_pos	 	= (16,80)	
		self.health_pos 	= (16,16)
		self.shield_pos 	= (16,32)
		self.wanted_level_pos 	= (16,48)
		self.credit_pos 	= (16,64)
		
	def update(self):
		self.health 		= "health: "+str(glo.health)
		self.shield 		= "shield: "+str(glo.shield)
		self.wanted_level 	= "wanted: "+str(glo.wanted_level)
		self.credit 		= "credit: "+str(glo.credit)	
		self.xp 		= "xp: "+str(glo.xp)	
	
	def draw(self,view):
		view.blit(self.font.render(self.health,1,glo.text_color),self.health_pos)
		view.blit(self.font.render(self.shield,1,glo.text_color),self.shield_pos)
		view.blit(self.font.render(self.credit,1,glo.text_color),self.credit_pos)
		view.blit(self.font.render(self.xp,1,glo.text_color),self.xp_pos)
		view.blit(self.font.render(self.wanted_level,1,glo.text_color),self.wanted_level_pos)

