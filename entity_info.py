#                entity information 
#
# starting templates for object information in the form of dictionaries. 
#
#
#
#------------------------------------------------------------------------------
#
# group- 	0 = player		1 = obstuction		2 = npc
#		3 = player enemy	4 = common enemy	5 = friend
#		6 = police
#
# remove_event- 0 = none		1 = impact_0		2 = impact_1
#		3 = impact_2		4 = roid_impact		5 = explode_0
#		6 = add_roid		7 = pick_up

# hostility- 	0 = non-hostile 		1 = hostile/running 
#             	2 = running/shooting 		3 = chacing/shooting 
#
#
#
#	images
from pygame import image

file_loc = "/home/matt/My_Programs/SPGA.001/";

image = (
	image.load(file_loc+'images/player_ship_0.png'),	#0
	image.load(file_loc+'images/npc0.png'),			#1
	image.load(file_loc+'images/npc1.png'),			#2
	image.load(file_loc+'images/roids_tiny.png'),		#3
	image.load(file_loc+'images/roids_sml.png'),		#4
	image.load(file_loc+'images/roids_med.png'),		#5
	image.load(file_loc+'images/roid_explode.png'),		#6
	image.load(file_loc+'images/impact_0.png'),		#7
	image.load(file_loc+'images/impact_0.png'),		#8
	image.load(file_loc+'images/impact_0.png'),		#9
	image.load(file_loc+'images/explode_0.png'),		#10
	image.load(file_loc+'images/explode_0.png'),		#11
	image.load(file_loc+'images/explode_0.png'),		#12	
	image.load(file_loc+'images/police_0.png'),		#13
	image.load(file_loc+'images/police_0.png'),		#14
	image.load(file_loc+'images/police_0.png'),		#15
	image.load(file_loc+'images/trader.png'),		#16
	image.load(file_loc+'images/trader.png'),		#17
	image.load(file_loc+'images/trader.png'),		#18
	image.load(file_loc+'images/background_0.png'),		#19	
	image.load(file_loc+'images/missile_0.png'),		#20
	image.load(file_loc+'images/thrust.png'),		#21
	image.load(file_loc+'images/sml_shield.png'),		#22
	image.load(file_loc+'images/pickups.png'),		#23
	image.load(file_loc+'images/thrust.png'),		#24
	image.load(file_loc+'images/sml_shield.png')		#25
	)
#
#	remember the (,)
#
#
#==============================================================================
# logical
player ={
	'group'			:'player',
	'health'		:1000,
	'max_health'		:1000,
	'shield'		:1000,
	'max_shield'		:1000,	
	'remove_event'		:2,
	'max_speed_x'		:7,
	'max_speed_y'		:5,
	'acceleration_x'	:2,
	'acceleration_y'	:1,
	'deceleration_x'	:.3,
	'deceleration_y'	:.3,
	'ai'			:False,
	'level'			:0,
	'controllable'		:True,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'image'			:0,
	'columns'		:2,
	'rows'			:1,
	'column'		:0,
	'row'			:0,
	'width'			:image[0].get_rect().width/2,
	'height'		:image[0].get_rect().height,
	'impact_damage'		:50,	
	'shield_regen_delay'	:3,
	'xp'			:10	
	}
#
#
npc_0  ={
	'group'			:'npc',
	'health'		:150,
	'max_health'		:150,
	'shield'		:500,
	'max_shield'		:500,	
	'remove_event'		:7,
	'max_speed_x'		:4,
	'max_speed_y'		:4,
	'acceleration_x'	:1,
	'acceleration_y'	:1,
	'deceleration_x'	:0.05,
	'deceleration_y'	:0.05,
	'border_ratio'		:1.5,
	'ai'			:True,
	'controllable'		:False,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'image'			:1,
	'level'			:1,
	'columns'		:2,
	'rows'			:6,
	'column'		:0,
	'row'			:0,
	'width'			:image[1].get_rect().width/2,
	'height'		:image[1].get_rect().height/7,
	'impact_damage'		:50,	
	'shield_regen_delay'	:3,
	'xp'			:30		
	}
#
npc_1  ={
	'group'			:'npc',
	'health'		:200,
	'max_health'		:200,
	'shield'		:600,
	'max_shield'		:600,	
	'remove_event'		:7,
	'max_speed_x'		:4,
	'max_speed_y'		:4,
	'acceleration_x'	:1,
	'acceleration_y'	:1,
	'deceleration_x'	:0.1,
	'deceleration_y'	:0.1,
	'border_ratio'		:1.5,
	'ai'			:True,
	'controllable'		:False,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'level'			:2,
	'image'			:2,
	'columns'		:2,
	'rows'			:6,
	'column'		:0,
	'row'			:0,
	'width'			:image[2].get_rect().width/2,
	'height'		:image[2].get_rect().height/14,
	'impact_damage'		:50,	
	'shield_regen_delay'	:3,
	'xp'			:30	
	}
#
npc_2  ={
	'group'			:'npc',
	'health'		:200,
	'max_health'		:200,
	'shield'		:800,
	'max_shield'		:800,	
	'remove_event'		:7,
	'max_speed_x'		:4,
	'max_speed_y'		:4,
	'acceleration_x'	:1,
	'acceleration_y'	:1,
	'deceleration_x'	:0.1,
	'deceleration_y'	:0.1,
	'border_ratio'		:1.5,
	'ai'			:True,
	'controllable'		:False,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'image'			:1,
	'level'			:3,
	'columns'		:2,
	'rows'			:6,
	'column'		:0,
	'row'			:0,
	'width'			:image[1].get_rect().width/2,
	'height'		:image[1].get_rect().height/7,
	'impact_damage'		:50,	
	'shield_regen_delay'	:3,
	'xp'			:30		
	}

#
police_0 ={
	'group'			:'police',
	'level'			:5,
	'health'		:100,
	'max_health'		:100,
	'shield'		:300,
	'max_shield'		:300,	
	'remove_event'		:7,
	'max_speed_x'		:5,
	'max_speed_y'		:4,
	'acceleration_x'	:2.5,
	'acceleration_y'	:2.5,
	'deceleration_x'	:0.2,
	'deceleration_y'	:0.2,
	'hostility'		:0,
	'border_ratio'		:1.6,
	'ai'			:True,
	'controllable'		:False,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'image'			:13,
	'columns'		:2,
	'rows'			:1,
	'column'		:0,
	'row'			:0,
	'width'			:image[13].get_rect().width/2,
	'height'		:image[13].get_rect().height,
	'animated'		:False,	
	'solid'			:True,
	'impact_damage'		:50,	
	'shield_regen_delay'	:3,
	'xp'			:100	
	}
#
#=============================================================================
# animated_solid
trader  ={
	'group'			:'trader',
	'health'		:100000,
	'max_health'		:100,
	'shield'		:300,
	'max_shield'		:300,	
	'remove_event'		:7,
	'max_speed_x'		:2,
	'max_speed_y'		:1,
	'weapon'		:1,
	'weapon_1_height'	:10,
	'level'			:20,
	'image'			:16,
	'columns'		:9,
	'rows'			:10,
	'column'		:0,
	'row'			:0,
	'width'			:image[16].get_rect().width/9,
	'height'		:image[16].get_rect().height/10,
	'impact_damage'		:100,
	'animation_delay'	:5,
	'xp'			:100	
	}
#
#
#=============================================================================
# simple solid
roid_0 ={
	'group'			:'roid',
 	'level'			:0,
	'health'		:100,
	'damage'		:40,
	'remove_event'		:3,
	'image'			:3,
	'row'			:0,
	'column' 		:2,
	'width'			:image[3].get_rect().width/4,
	'height'		:image[3].get_rect().height,
	'impact_damage'		:15,
	'xp'			:10,
	'rotating'		:True		
	}
#
roid_1 ={
	'group'			:'roid',
 	'level'			:0,
	'health'		:200,
	'damage'		:40,
	'remove_event'		:4,
	'image'			:4,
	'row'			:0,
	'column' 		:2,
	'width'			:image[4].get_rect().width/4,
	'height'		:image[4].get_rect().height,
	'impact_damage'		:50,
	'xp'			:10,
	'rotating'		:True		
	}
#
roid_2 ={
	'group'			:'roid',
 	'level'			:0,
	'health'		:300,
	'damage'		:40,
	'remove_event'		:5,
	'image'			:5,
	'row'			:0,
	'column' 		:2,
	'width'			:image[5].get_rect().width/4,
	'height'		:image[5].get_rect().height,
	'impact_damage'		:100,
	'xp'			:10,
	'rotating'		:True		
	}
#
roid_3 ={
	'group'			:'roid',
 	'level'			:0,
	'health'		:60,
	'damage'		:40,
	'remove_event'		:6,
	'image'			:5,
	'row'			:0,
	'column' 		:2,
	'width'			:image[5].get_rect().width/4,
	'height'		:image[5].get_rect().height,
	'impact_damage'		:50,
	'xp'			:10,
	'rotating'		:True		
	}
#
missile_0 ={
	'group'			:'missile',
	'owner'			:None,
	'health'		:1,
	'level'			:1,
	'remove_event'		:1,
	'image'			:20,
	'column'		:0,
	'row'			:0,
	'width'			:image[20].get_rect().width,
	'height'		:image[20].get_rect().height,
	'impact_damage'		:300,
	'rotating'		:False	
	}
#
pickup ={
	'group'			:'pickup',
	'level'			:1,
	'health'		:10,
	'damage'		:40,
	'remove_event'		:0,
	'image'			:23,
	'row'			:0,
	'column' 		:0,
	'width'			:image[23].get_rect().width/4,
	'height'		:image[23].get_rect().height,
	'impact_damage'		:0,
	'xp'			:10,
	'rotating'		:True		
	}

#	
#==============================================================================
# simple_ghost
background_0 ={
	'group'			:'scenery',
	'image'			:19,
	'column'		:0,
	'row'			:0,
	'width'			:image[19].get_rect().width,
	'height'		:image[19].get_rect().height,
	}	
#	
#==============================================================================
# animated_ghost
impact_0 ={
	'group'			:'explosion',
	'remove_event'		:0,
	'image'			:7,
	'column'		:0,
	'row'			:0,
	'columns'		:3,
	'rows'			:2,
	'width'			:image[7].get_rect().width/3,
	'height'		:image[7].get_rect().height/2,
	'impact_damage'		:60,
	'animation_delay'	:4,	
	}
#
explosion_0 ={
	'group'			:'explosion',
	'remove_event'		:0,
	'image'			:10,
	'column'		:0,
	'row'			:0,
	'columns'		:3,
	'rows'			:2,
	'width'			:image[10].get_rect().width/5,
	'height'		:image[10].get_rect().height/2,
	'impact_damage'		:60,
	'animation_delay'	:5,	
	}
#
roid_explode ={
	'group'			:'explosion',
	'remove_event'		:0,
	'image'			:6,
	'column'		:0,
	'row'			:0,
	'columns'		:3,
	'rows'			:2,
	'width'			:image[6].get_rect().width/4,
	'height'		:image[6].get_rect().height/2,
	'impact_damage'		:60,
	'animation_delay'	:4,	
	}
#
thruster_0 ={
	'group'			:'thruster',
	'owner'			:None,
	'remove_event'		:0,
	'image'			:21,
	'column'		:0,
	'row'			:0,
	'columns'		:3,
	'rows'			:2,
	'width'			:image[21].get_rect().width/3,
	'height'		:image[21].get_rect().height/2,
	'impact_damage'		:60,
	'animation_delay'	:4,	
	}
#
shield_0 ={
	'group'			:'shield',
	'owner'			:None,
	'health'		:1,
	'remove_event'		:0,
	'image'			:22,
	'column'		:0,
	'row'			:0,
	'columns'		:3,
	'rows'			:2,
	'width'			:image[22].get_rect().width/5,
	'height'		:image[22].get_rect().height/4,
	'impact_damage'		:60,
	'animation_delay'	:4,	
	}
#	


