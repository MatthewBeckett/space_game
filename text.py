from pygame import font
import globle as glo
from random import randint

class text:
	def __init__(self,text,color,pos,frames):
		self.text 	= str(text)
		self.pos 	= pos
		self.frames 	= frames
		self.frame	= 0
		self.color	= color
		
		self.font 	= font.SysFont("DejaVu Sans",15)
		self.remove	= False
		
		self.xm = randint(-1,1)
		self.ym = randint(-1,1)
	
		self.pos = (self.pos[0] + self.xm,	self.pos[1] + self.ym)

	def update(self):
	
		self.frame +=1
		if self.frame > self.frames:
			self.remove = True
		
		self.pos = (self.pos[0] - glo.player_speed_x, self.pos[1])
	
		self.pos = (self.pos[0] + self.xm,	self.pos[1] + self.ym)


	def draw(self,view):
		view.blit(self.font.render(self.text,1,self.color),self.pos)
		
