import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	pygame.init()
	game_settings = Settings()
	game_stats = GameStats(game_settings)
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	scoreboard = Scoreboard(game_settings, screen, game_stats)
	pygame.display.set_caption("Alein Invasion")
	play_button = Button(game_settings, screen, "Play")
	highscore_button = Button(game_settings, screen, "Highscores")
	
	ship = Ship(screen, game_settings)
	bullets = Group()
	aliens = Group()
	#gf.create_fleet(game_settings, game_stats, screen, ship, aliens)
	
	pygame.mixer.music.load(game_settings.bgm)
	pygame.mixer.music.play(-1)
	

	#Start the main loop of the game
	while True:
		gf.check_events(game_settings, screen, game_stats, scoreboard, 
			play_button, highscore_button, ship, aliens, bullets)
		
		if game_stats.game_active:
			ship.update() 
			gf.update_bullets(game_settings, game_stats, scoreboard, screen, 
				ship, bullets, aliens)		
			gf.update_aliens(game_settings, game_stats, screen, scoreboard, 
				ship, bullets, aliens)
			
		gf.update_screen(game_settings, game_stats, scoreboard, screen, ship, 
			bullets, aliens, play_button, highscore_button)
		game_stats.tick()
		
run_game()
