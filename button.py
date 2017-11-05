#import pygame.font
import pygame

class Button():
	
	def __init__(self, game_settings, screen, message):
		"""intialise button attributes"""
		self.screen = screen
		self.screen_rect= screen.get_rect()
		
		#set the dimensions and properties of the button
		self.width = 200
		self.height = 50
		self.button_color = (0,255,0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		#build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		self.prep_msg(message)
		
	def prep_msg(self, message):
		"""turn message into into an image and center text on  the button"""
		self.msg_image = self.font.render(message, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		pygame.draw.rect(self.screen, self.button_color, self.rect)
		#self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)