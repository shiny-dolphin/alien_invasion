import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet"""

	
	def __init__(self, game_settings, game_stats, screen):
		"""Intitalise the alien and set its starting position."""
		super().__init__()
		self.screen = screen
		self.game_settings = game_settings
		self.game_stats = game_stats
		
		#sort out alien color and image
		self.red = False
		self.blue = False
		self.green = False
		self.image_color = self.find_image_color(self.game_stats.level)
		
		self.image = pygame.image.load(self.image_color)
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the aliens exact position. 
		self.x = float(self.rect.x)
		

	def find_image_color(self, difficulty_level):
		red_max = difficulty_level * 4
		blue_max = difficulty_level * 4 + red_max
		random_number = random.randint(0,100)
		if random_number < red_max:
			self.red = True
			return 'images/alien_red.bmp'
		elif random_number < blue_max:
			self.blue = True
			return 'images/alien_blue.bmp'
		else:
			self.green = True
			return 'images/alien.bmp'			

	
	def check_edges(self):
		"""return true if alien is at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			

	def update(self):
		"""move the alien to the left and right"""
		self.x += self.game_settings.alien_speed * self.game_settings.fleet_direction
		self.rect.x = self.x
	
	
	def blitme(self):
		"""Draw the alien at its current location"""
		self.screen.blit(self.image, self.rect)