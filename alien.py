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
		
		#sort out alien color, score value and image
		self.red = False
		self.blue = False
		self.green = False
		self.point_value = 0
		self.image_color = ''
		self.set_up_alien_color()

		self.image = pygame.image.load(self.image_color)
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the aliens exact position. 
		self.x = float(self.rect.x)
		

	def set_up_alien_color(self):
		"""sets the color of the alien Spawn rates for stronger red and blue 
		aliens increase with level"""
		difficulty_level = self.game_stats.level * 4
		red_max = difficulty_level
		blue_max = difficulty_level + red_max
		random_number = random.randint(0,100)
		if random_number < red_max:
			self.red = True
			self.point_value = self.game_settings.alien_points_red
			self.image_color =  'images/alien_red.bmp'
		elif random_number < blue_max:
			self.blue = True
			self.point_value = self.game_settings.alien_points_blue
			self.image_color = 'images/alien_blue.bmp'
		else:
			self.green = True
			self.point_value = self.game_settings.alien_points_green
			self.image_color = 'images/alien.bmp'		

	def change_color(self):
		"""changes the color and image of hit alien"""
		if self.green:
			return False	
		elif self.red:
			self.red = False
			self.blue = True
			self.image = pygame.image.load('images/alien_blue.bmp')
			return True
		elif self.blue:
			self.blue = False
			self.green = True
			self.image = pygame.image.load('images/alien.bmp')
			return True

	
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