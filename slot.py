import pygame

_number_of_input_buttons = 0

class Slot():

	def __init__(self, game_settings, screen):
		"""makes a slot which is used for user name input after game over"""
		self.active = False
		self.game_settings = game_settings
		self.screen = screen
		self.screen_rect= screen.get_rect()
		
		self.input_values = ['A','B','C','D','E','F','G','H','I','J','K',
			'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
			'0', '1','2','3','4','5','6','7','8','9']
			
		self.current_index = 0
		self.character = self.input_values[0]
		self.make_slot()


		
	def make_slot(self):
		global _number_of_input_buttons

		self.width = 80
		self.height = 80
		self.button_color = (40,40,40)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 88)
		self.rect = pygame.Rect(0,0,self.width, self.height)
		
		#variables to adjust the slots
		gap = 40
		adjustment = _number_of_input_buttons * (self.width + gap)
		screen_width = self.game_settings.screen_width
		
		x_value = ((screen_width - (3 * self.width + (2*gap)))/2) + adjustment
		self.rect.x = x_value
		self.rect.centery = self.screen_rect.centery
		
		_number_of_input_buttons += 1
		self.prep_character(self.character, self.rect.centerx, self.rect.centery)


		
	def prep_character(self, character, centerx, centery):
		"""turn character into into an image and center text on  the button"""
		self.charac_image = self.font.render(character, True, self.text_color, 
			self.button_color)
		self.charac_image_rect = self.charac_image.get_rect()
		self.charac_image_rect.centerx = centerx
		self.charac_image_rect.centery = centery


		
	def move_character_up(self):
		"""changes the character displayed in the slot"""
		if abs(self.current_index) == len(self.input_values) - 1:
			self.current_index = 0
		self.current_index += 1
		self.character = self.input_values[self.current_index]
		self.prep_character(self.character, self.rect.centerx, self.rect.centery)

		
	
	def move_character_down(self):
		"""changes the character displayed in the slot"""
		if abs(self.current_index) == len(self.input_values) - 1:
			self.current_index = 0
		self.current_index -= 1
		self.character = self.input_values[self.current_index]
		self.prep_character(self.character, self.rect.centerx, self.rect.centery)


		
	def draw_slot(self):
		pygame.draw.rect(self.screen, self.button_color, self.rect)
		self.screen.blit(self.charac_image, self.charac_image_rect)
		
		
		
		
		
		
		
		
		