import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets):
	"""respond to key presses"""
	if event.key == pygame.K_RIGHT:
		#ship.moving_left = False
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#ship.moving_right = False
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

		

def fire_bullet(game_settings, screen, ship, bullets):
	if len(bullets) < game_settings.bullets_allowed:
		new_bullet = Bullet(game_settings, screen, ship)
		bullets.add(new_bullet)


		
def check_keyup_events(event, ship):
	"""respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key ==  pygame.K_LEFT:
		ship.moving_left = False
		

		
def check_events(game_settings, screen, game_stats, scoreboard, play_button, ship, aliens,
		bullets):
	"""Respond to keypresses and mouse events"""
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, game_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(game_settings, screen, game_stats, scoreboard, play_button,
				ship, aliens, bullets, mouse_x, mouse_y)
			
			
			
def check_play_button(game_settings, screen, game_stats, scoreboard, play_button, ship,
		aliens, bullets, mouse_x, mouse_y):
	"""start a new game when the player clicks the play button"""
	play_button_pushed = play_button.rect.collidepoint(mouse_x, mouse_y) 
	if play_button_pushed and not game_stats.game_active:
		#reset the speed of ship, bullets and aliens
		game_settings.reset()
		pygame.mouse.set_visible(False)
		start_game(game_settings, screen, game_stats, scoreboard, ship, aliens,
			bullets)


		
def start_game(game_settings, screen, game_stats, scoreboard, ship, aliens, 
		bullets):
	#reset the game stats
	game_stats.reset_stats()
	game_stats.game_active = True
	
	#reset the scoreboard
	scoreboard.prep_score()
	scoreboard.prep_high_score()
	scoreboard.prep_level()
	scoreboard.prep_lives()
	
	#empty the alien and bullet lists
	aliens.empty()
	bullets.empty()
	
	#create the alien fleet and center our ship
	create_fleet(game_settings, screen, ship, aliens)
	ship.center_ship()

	
					
def update_screen(game_settings, game_stats, scoreboard, screen, ship, 
			bullets, aliens, play_button):
	"""Update images on the screen and flip to the new screen"""
	
	screen.fill(game_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	aliens.draw(screen)
	scoreboard.show_score()
	
	if not game_stats.game_active:
		play_button.draw_button()
	
	#Make the most recently drawn screen visible
	pygame.display.flip()
	
	
def check_high_score(game_stats, scoreboard):
	"""See if there is a new high score, called from check_collisions func"""

	if game_stats.score > game_stats.high_score:
		game_stats.high_score = game_stats.score
		scoreboard.prep_high_score()
	
def update_bullets(game_settings, game_stats, scoreboard, screen, ship, 
		bullets, aliens):
	#Calls update() for each bullet we put in the group
	bullets.update()
	
	#Get rid of bullets that have left the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_collisions(game_settings, game_stats, scoreboard, screen, ship, 
		bullets, aliens)

	
	
def check_collisions(game_settings, game_stats, scoreboard, screen, ship, 
		bullets, aliens):
	#Check for collisions between bullets and aliens, removes both
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	#updates the points
	if collisions:
		for aliens in collisions.values():
			game_stats.score += game_settings.alien_points *len(aliens)
			scoreboard.prep_score()
		check_high_score(game_stats, scoreboard)	
	
	#repopulate fleet if no aliens left
	if len(aliens) <= 0:
		bullets.empty()
		game_settings.increase_speed()
		
		#Increase the level
		game_stats.level += 1
		scoreboard.prep_level()
		
		create_fleet(game_settings, screen, ship, aliens)
	
	
	
def get_number_aliens_x(game_settings, alien_width):
	available_space_x = game_settings.screen_width - (2 * alien_width)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

	
	
def create_alien(game_settings, screen, aliens, alien_number, row_number):
	alien = Alien(game_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	
	alien_height = alien.rect.height
	alien.rect.y = alien_height + 2 * alien_height * row_number
	aliens.add(alien)

	
	
def get_number_rows(game_settings, ship_height, alien_height):
	availabe_space_y = (game_settings.screen_height - 
		(alien_height * 3) - ship_height)
	number_rows = int(availabe_space_y / (2 * alien_height))
	return number_rows
		
	
	
def create_fleet(game_settings, screen, ship, aliens):
	"""Creates the alien fleet"""
	alien = Alien(game_settings, screen)
	number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
	number_rows = get_number_rows(game_settings, ship.rect.height, 
		alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(game_settings, screen, aliens, alien_number, row_number)

			
			
def check_fleet_edges(game_settings, aliens):
	"""Checks each alien if it has hit the edge of the screen, if it has 
	change directions"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(game_settings, aliens)
			break

			
			
def change_fleet_direction(game_settings, aliens):
	"""after hitting an edge, move aliens down and change the direction the 
	fleet is moving in"""
	for alien in aliens.sprites():
		alien.rect.y += game_settings.fleet_drop_speed
	game_settings.fleet_direction *= -1

	
	
def ship_hit(game_settings, game_stats, screen, scoreboard, ship, bullets, aliens):
	"""if ship is hit, check if we still have lives left otherwise end the game"""
	if game_stats.ships_left > 0:
		game_stats.ships_left -= 1
		scoreboard.prep_lives()
		aliens.empty()
		bullets.empty()
		create_fleet(game_settings, screen, ship, aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		game_stats.game_active = False
		pygame.mouse.set_visible(True)
	
	

def check_bottom(game_settings, game_stats, screen, scoreboard,ship, bullets, aliens):
	"""checks if aliens has hit bottom of the screen"""
	for alien in aliens.sprites():
		if alien.rect.bottom >= game_settings.screen_height:
			ship_hit(game_settings, game_stats, screen, scoreboard, ship, bullets, aliens)
			break
	


def update_aliens(game_settings, game_stats, screen, scoreboard, ship, bullets, aliens):
	"""handles moving the alien and checking to if anything has been hit"""
	aliens.update()
	check_fleet_edges(game_settings, aliens)
	
	#Look for alien ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(game_settings, game_stats, screen, scoreboard, ship, bullets, aliens)
		
	#look for aliens hitting bottom
	check_bottom(game_settings, game_stats, screen, scoreboard, ship, bullets, aliens)
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	