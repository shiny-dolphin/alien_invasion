import pygame

class GameStats():
	"""Track statistics for alien invastion"""
	
	def __init__(self, game_settings):
		self.game_settings = game_settings
		self.reset_stats()
		self.game_active = False
		
		#clock, game won't run faster than 360 frames per second.
		#keeps things smooth
		self.clock = pygame.time.Clock()
		self.FPS = 360
		self.play_time = 0
		
		#High Scores
		self.high_score = 0

	def tick(self):
		self.clock.tick(self.FPS)
		
	def reset_stats(self):
		self.ships_left = self.game_settings.ship_limit
		self.score = 0
		self.level = 1