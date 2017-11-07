import pygame
import pygame.font
import sys

from button import Button
from slot import Slot


def game_over_screen(game_settings, game_stats, screen):
	#image and rect for printing game over at the top of the screen
	image = pygame.image.load('images/game_over.bmp')
	image_rect = image.get_rect()
	screen_rect = screen.get_rect()
	image_rect.centerx = screen_rect.centerx
	image_rect.top = screen_rect.top
	
	#show high score and give user instructions
	font = pygame.font.SysFont(None, 48)
	score = round(game_stats.score, -1)
	score_str = "{:,}".format(score)
	message = []
	message.append("YOU GOT A HIGHSCORE OF " + score_str + ".")
	message.append("ENTER YOUR NAME")
	message.append("USE THE UP AND DOWN KEYS TO CHANGE THE LETTER")
	message.append("PRESS RETURN TO CONFIRM SELECTION")
	message_image = font.render('nothing', True, (255,255,255),(0,0,0))
	
	message.reverse()
		
	#make 3 slots for entering characters, set the first one to active
	slot_1 = Slot(game_settings, screen)
	slot_2 = Slot(game_settings, screen)
	slot_3 = Slot(game_settings, screen)
	slot_1.active = True
	slot_2.active = False
	slot_3.active = False
	slots = [slot_1, slot_2, slot_3]
	
	#moveable border to show player which slot is active
	border = Button(game_settings, screen, '', 'border')
	
	while True:
		screen.fill((0,0,0))
		
		#Draw the three slots, they're in a list
		for slot in slots:
			slot.draw_slot()
	
		#Draw the moveable frame
		border.draw_border()
		
		#draw the game over image and the instructions
		screen.blit(image, image_rect)
		rect_y = screen_rect.bottom - 50
		for lines in message:
			message_image = font.render(lines, True, (255,255,255),(0,0,0))
			message_rect = message_image.get_rect()
			message_rect.centerx = screen_rect.centerx
			message_rect.bottom = rect_y
			screen.blit(message_image, message_rect)
			rect_y -= 35
			
		
		check_events(border, slots)		
		pygame.display.flip()

		
def check_events(border, slots):
	"""check if the return button in the highscore screen is pushed"""
	for event in pygame.event.get():	
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				move_active_slot(slots)
				for slot in slots:
					if slot.active:
						border.make_border()
			if event.key == pygame.K_UP:
				for slot in slots:
					if slot.active:
						slot.move_character_up()
			if event.key == pygame.K_DOWN:
				for slot in slots:
					if slot.active:
						slot.move_character_down()

				
			
def move_active_slot(slots):
	for x in range(0,3):
		if x == 0 and slots[x].active:
			slots[x].active = False
			slots[x+1].active = True
			break
		elif x == 1 and slots[x].active:
			slots[x].active = False
			slots[x+1].active = True
			break
		elif x == 2 and slots[x].active:
			slots[x].active = False
			break


			
			