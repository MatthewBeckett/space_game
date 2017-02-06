# # # # # #___ Globle Variables ___# # # # # # #
#
#--------------------------------------------------------------
#		Static
#--------------------------------------------------------------
#
#	Pygame Window
window_caption		= 'Space Game'
screen_width		= 1366
screen_height		= 768
fps			= 50
#
#	Max Objets
max_entities		= 100
#
#
#	Spawn Rates - per 10 minutes at 60 fps
roid_spawn_rate		= 20000
npc_spawn_rate		= 10000
police_spawn_rate	= 100
trader_spawn_rate	= 10
#
#
max_up			= 0
max_down		= screen_height - 64
max_left		= 256
max_right		= screen_width * 0.60 
#
#	Weapon Fire Rates
fire_rate_0		= 4
#
#	Hud
text_color		= (255,255,255)
#
#--------------------------------------------------------------
#		Active
#--------------------------------------------------------------
#
#
#	Object ID
ID		= 0
#	
#	Player stats
health		= 0
shield		= 0
wanted		= 0
credit		= 0
wanted_level	= 0
xp		= 0
#
#	Player Alive
player_alive	= True
#	Player Speed
player_speed_x 		= 0
#
#	Player pos
player_pos_x		= 0
player_pos_y		= 0
# 
#	Player ID
player_id		= 0
#
#	Frame Counter
frame_count		= 0
#
#	Missile Start Location List (x(int),y(int))
missile_0		= []*0
#
#	Remove events
remove_event		= []*0
#
#	Object Lists
#
#	Text
text			= []*0
#
#	Key presses
pressing_up 		= False 
pressing_down 		= False 
pressing_left 		= False 
pressing_right		= False 
pressing_space		= False
pressing_ctrl		= False
pressing_shift		= False
pressing_z		= False
pressing_t		= False
#
#
#
#
#





