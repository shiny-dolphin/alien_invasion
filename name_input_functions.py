import pygame

from button import Button


def game_over_screen(game_settings, game_stats, screen):
	#print game over at top
	
	input_values = ['A','B','C','D','E','F','G','H','I','J','K',
		'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		'0', '1','2','3','4','5','6','7','8','9']
	
	message = 'A'
	#make 3 slots to input name
	slot_one = Button(game_settings, screen, message, position='one')
	#slot_two = Button(game_settings, screen, message, position='two')
	#slot_three = Button(game_settings, screen, message, position='three')
	
	slot_one.adjust_button_position()
	#slot_two.set_position()
	#slot_three.set_position()
	
	while True:
		screen.fill(game_settings.highscore_screen_color)
		slot_one.draw_button()
		#slot_two.draw_button()
		#slot_three.draw_button()		
		pygame.display.flip()



	