import pygame
import json

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
		self.filename = 'highscore.json'
		self.highscore_all = []
		self.load_hi_score()

		

	def tick(self):
		self.clock.tick(self.FPS)


		
	def reset_stats(self):
		self.ships_left = self.game_settings.ship_limit
		self.score = 0
		self.level = 1
		

				
	def save_hi_score(self, player_name):
		#highscore_list = [(13552, 'ZAC'),(3341, 'ME'),(333, 'Hafo'), (444, 'Kim')]
		#sorted_highscore_list = sorted(highscore_list, key= lambda player : player[0])
		#sorted_highscore_list.reverse()
		#for entry in sorted_highscore_list:
		#	print("SCORE: {} .... NAME: {}".format(entry[0], entry[1]))
		
		player = (self.score, self.level, player_name)
		self.highscore_all.append(player)
		print("saving " + player_name + "'s hiscore")
		with open(self.filename, 'w') as f_obj:
			json.dump(self.highscore_all, f_obj)
	
	
	
	def load_hi_score(self):
		try:
			with open(self.filename) as f_obj:
				self.highscore_all = json.load(f_obj)
				self.highscore_all = sorted(self.highscore_all, 
					key= lambda player : player[0])
				self.highscore_all.reverse()
				top_player = self.highscore_all[0]
				self.high_score = top_player[0]
				self.top_player_name = top_player[2]
				
		except FileNotFoundError:
			pass
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			