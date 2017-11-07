#import pygame.font
import pygame


#Global variable to track total number of buttons
_number_of_menu_buttons = 0
_border_position = 0

class Button():

	def __init__(self, game_settings, screen, message, button_type=''):
		"""intialise button attributes"""
		self.game_settings = game_settings
		self.screen = screen
		self.screen_rect= screen.get_rect()
		self.button_type = button_type
		self.message = message
		
		if self.button_type=='menu':
			self.make_menu_button()
		elif self.button_type=='return':
			self.make_return_button()
		elif self.button_type=='border':
			self.make_border()
			

		
	def make_menu_button(self):
		"""Makes the menu buttons visible when the game first starts"""
		global _number_of_menu_buttons
		_number_of_menu_buttons += 1
		
		#set the dimensions and properties of the button
		self.width = 200
		self.height = 50
		self.button_color = (0,255,0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		#build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		adjust_distance = _number_of_menu_buttons * self.height * 1.2
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery + adjust_distance
		
		self.prep_msg(self.message, self.rect.centerx, self.rect.centery)
	
	
	
	def make_return_button(self):
		"""Makes the button which returns to the main screen after entering
		the highscores page"""
		#set the dimensions and properties of the button
		self.width = 200
		self.height = 50
		self.button_color = (0,255,0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom -20

		self.prep_msg(self.message, self.rect.centerx, self.rect.centery)
		
		
		
	def make_border(self):
		"""makes a moveable border to indicate to the player which slot is
		currently selected for character input"""
		global _border_position
		self.width = 80
		self.height = 80
		self.button_color = (0,255,0)
		self.rect = pygame.Rect(0,0,self.width, self.height)
		
		gap = 40
		adjustment = _border_position * (self.width + gap)
		screen_width = self.game_settings.screen_width
		
		x_axis = ((screen_width - (3 * self.width + (2*gap)))/2) + adjustment
		self.rect.x = x_axis
		self.rect.centery = self.screen_rect.centery
		_border_position += 1


		
	def prep_msg(self, message, centerx, centery):
		"""turn message into into an image and center text on  the button"""
		self.msg_image = self.font.render(message, True, self.text_color, 
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = centerx
		self.msg_image_rect.centery = centery
		
		
		
	def draw_button(self):
		pygame.draw.rect(self.screen, self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
		
		
	def draw_border(self):
		"""draws the moveable border"""
		pygame.draw.rect(self.screen, self.button_color, self.rect, 5)
		
		
		
		

		