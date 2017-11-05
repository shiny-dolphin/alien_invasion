import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, screen, game_settings):
		
		super().__init__()
		self.screen = screen
		self.game_settings = game_settings
		
		#Load the ship image and get get rectangles for ship image and screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		#Direction of movement flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.game_settings.ship_speed
		
		#rect.centerx only stores integers, self.enter is truncated
		self.rect.centerx = self.center
		
	def center_ship(self):
		self.center = self.screen_rect.centerx
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		