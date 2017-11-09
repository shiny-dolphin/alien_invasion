import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""Report the score"""
	
	def __init__(self, game_settings, screen, game_stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.game_settings = game_settings
		self.game_stats = game_stats
		
		#font ad color setting for the scoreboard
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_lives()
		
	def prep_score(self):
		"""Turn the score into an image"""
		rounded_score = round(self.game_stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.game_settings.bg_color)
		
		#display the score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def prep_high_score(self):
		"""Turn high score into an image"""
		rounded_high_score = round(self.game_stats.high_score, -1)
		high_score_str = "High Score:  {:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str, True, 
			self.text_color, self.game_settings.bg_color)
			
		#Center high score at the top of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20
		
	def prep_level(self):
		level_str = "LVL: " + str(self.game_stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color,
			self.game_settings.bg_color)
		
		#position level below current score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.top = self.score_rect.bottom + 10
		self.level_rect.right = self.screen_rect.right - 20
	
	def prep_lives(self):
		"""Show how many lives the player has left"""
		self.ships = Group()
		for ship_number in range(self.game_stats.ships_left):
			ship = Ship(self.screen, self.game_settings)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def show_score(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
		
	def get_player_score(self):
		return 
		