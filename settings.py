class Settings():
	"""A Class to store all settings for Alien Invasion"""
	
	def __init__(self):
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.highscore_screen_color = (50, 50, 50)
		
		#Ship settings
		self.ship_speed = 2
		self.ship_limit = 3
		
		#Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
		
		#Alien Settings
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		
		#fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		
		#How quickly the game speeds up
		self.speed_up_scale = 1.08
		
		#Scoring
		self.alien_points_green = 50
		self.alien_points_blue = 150
		self.alien_points_red = 250
		self.score_scale = 1.1
		
		#Sounds and where they are located. 
		self.shoot = 'sounds/shoot.wav'
		self.hit_1 = 'sounds/hit_1.wav'
		self.hit_2 = 'sounds/hit_2.wav'
		self.alien_destroyed = 'sounds/alien_destroyed.wav'
		self.ship_destroyed = 'sounds/ship_destroyed.wav'
		self.bgm = 'sounds/bgm.mp3'
		
		
	def reset(self):
		self.bullet_speed_factor = 1
		self.ship_speed = 2
		self.alien_speed = 1
		self.fleet_direction = 1
		self.alien_points = 50
		self.alien_points_blue = 100
		self.alien_points_red = 200
		
	def increase_speed(self):
		self.ship_speed *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed *= self.speed_up_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		self.alien_points_red = int(self.alien_points_red * self.score_scale)
		self.alien_points_blue = int(self.alien_points_blue * self.score_scale)