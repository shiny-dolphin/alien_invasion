import pygame

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
	exit_button = Button(game_settings, screen, 'Return')
	exit_button.adjust_button_position()
	
	#Continue to display rankings until 'return' button is pushed
	while True:
		screen.fill(game_settings.highscore_screen_color)
		exit_button.draw_button()
		if check_return_button_pushed(exit_button):
			break			
		pygame.display.flip()
		

		
def check_return_button_pushed(exit_button):
	"""check if the return button in the highscore screen is pushed"""
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			exit_button_pushed = exit_button.rect.collidepoint(mouse_x, mouse_y)
			return exit_button_pushed