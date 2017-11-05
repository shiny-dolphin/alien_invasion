class Settings():
	"""A Class to store all settings for Alien Invasion"""
	
	def __init__(self):
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
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
		self.speed_up_scale = 1.1
		
		#Scoring
		self.alien_points = 50
		self.alien_points_blue = 100
		self.alien_points_red = 200
		self.score_scale = 1.5
		
		
	def reset(self):
		self.bullet_speed_factor = 1
		self.ship_speed = 2
		self.alien_speed = 1
		self.fleet_direction = 1
		self.alien_points = 50
		
	def increase_speed(self):
		self.ship_speed *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed *= self.speed_up_scale
		self.alien_points = int(self.alien_points * self.score_scale)