import pygame
import sys

from button import Button


def check_highscore_button(game_settings, screen, game_stats, scoreboard,
		highscore_button, mouse_x, mouse_y):
	"""checks if the highscore button is pushed"""
	highscore_button_pushed = highscore_button.rect.collidepoint(mouse_x, mouse_y)
	if highscore_button_pushed and not game_stats.game_active:
		draw_highscore_screen(game_settings, screen, game_stats, scoreboard)


		
def draw_highscore_screen(game_settings, screen, game_stats, scoreboard):
	"""changes the screen to display the rankings table"""
	#Make an exit button so game can return to main screen
	exit_button = Button(game_settings, screen, 'Return', 'return')
	top_five_players = game_stats.get_top_five()
	headings = ['RANK', 'SCORE', 'LEVEL', 'NAME']
	top_five_players.insert(0, headings)
	
	#Continue to display rankings until 'return' button is pushed
	while True:
		screen.fill(game_settings.highscore_screen_color)
		exit_button.draw_button()
		draw_title(game_settings, screen)
		for index in range(0, len(top_five_players)):
			draw_player(game_settings, top_five_players[index], index, screen)

		if check_return_button_pushed(exit_button):
			break			
		pygame.display.flip()

		
		
def draw_title(game_settings, screen):
	"""Draws the title 'TOP 5'.""" 
	font = pygame.font.SysFont(None, 80)
	rect = pygame.Rect(0, 0, 250, 50)
	rect.centerx = game_settings.screen_width / 2
	rect.centery = 80
	
	msg_image = font.render('TOP 5', True, (255, 0, 0), (50, 50, 50))
	msg_image_rect = msg_image.get_rect()
	msg_image_rect.centerx = rect.centerx
	msg_image_rect.centery = rect.centery
	
	pygame.draw.rect(screen,(50, 50, 50), rect)
	screen.blit(msg_image, msg_image_rect)
	
	
	
def draw_player(game_settings, player, index, screen):
	"""draws player info to high score screen"""
	width = 250
	height = 50
	font = pygame.font.SysFont(None, 48)
	text_color = (0, 0, 0)
	
	rect = pygame.Rect(0, 0, width, height)
	rect.top = 50 * (index + 1) + 150
	rect.centerx = game_settings.screen_width / 5
	
	#index 0 is the headings. 
	if index == 0:
	
		for item in player:
			if(item == 'RANK'):
				text_color = (255, 255, 0)
			else:
				text_color = (255, 255, 255)
				
			msg_image = font.render(item, True, text_color, (50, 50, 50))
			msg_image_rect = msg_image.get_rect()
			msg_image_rect.centerx = rect.centerx
			msg_image_rect.centery = rect.centery
			pygame.draw.rect(screen,(50, 50, 50), rect)
			screen.blit(msg_image, msg_image_rect)
			rect.centerx += game_settings.screen_width / 5
	
	else:
		text_color = (255, 255, 0)
		msg_image = font.render(str(index), True, text_color, (50, 50, 50))
		msg_image_rect = msg_image.get_rect()
		msg_image_rect.centerx = rect.centerx
		msg_image_rect.centery = rect.centery
		pygame.draw.rect(screen,(50, 50, 50), rect)
		screen.blit(msg_image, msg_image_rect)
		
		rect.centerx += game_settings.screen_width / 5
		text_color = (255, 255, 255)
		
		for item in player:
			msg_image = font.render(str(item), True, text_color, (50, 50, 50))
			msg_image_rect = msg_image.get_rect()
			msg_image_rect.centerx = rect.centerx
			msg_image_rect.centery = rect.centery
			pygame.draw.rect(screen,(50, 50, 50), rect)
			screen.blit(msg_image, msg_image_rect)
			rect.centerx += game_settings.screen_width / 5
			

		
def check_return_button_pushed(exit_button):
	"""check if the return button in the highscore screen is pushed"""
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			exit_button_pushed = exit_button.rect.collidepoint(mouse_x, mouse_y)
			return exit_button_pushed