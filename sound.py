import pygame
import os

_sound_library = {}

def play_sound(path):
	global _sound_library
	sound = _sound_library.get(path)
	if sound == None:
		 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		 sound = pygame.mixer.Sound(canonicalized_path)
		 sound.set_volume(0.5)
		 _sound_library[path] = sound
		 
	sound.play()