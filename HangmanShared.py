hangman_words = {
	'bc people name' : [('samuel', 'sensei'), ('andreas', 'mini version'), ('dewi', 'overlord'), ('otto', 'silver'), ('Indri', 'sensei\'s sensei')],
	'body part' : [('eye', '2c'), ('foot', 'journey'), ('belly', 'fat'), ('finger', 'touch'), ('heart', 'DEG DEG DEG')],
	'fruit' : [('watermelon', 'cocomelon'), ('banana', 'long'), ('lemon', 'life gives'), ('orange', 'sunset'), ('tomato', 'controversial')]
}

import time
import random
import sys
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

def wait_for(waiting_time_in_seconds):
	time.sleep(waiting_time_in_seconds)

def print_dialog(speech, speaker = ''):
	if speaker == 'Ghost Fiona: ' or speaker == 'Spirit: ':
		set_color_to('green')

	elif speaker == 'King Pascal: ' or speaker == 'Little Pascal: ' or speaker == 'Humongous Pascal: ':
		set_color_to('yellow')
	
	elif speaker == 'Unknown: ' or speaker == 'Prince Emil: ':
		set_color_to('cyan')

	else:
		set_color_to('white')

	print('')
	print(speaker + speech)
	wait_for(1.5)

def set_color_to(color):
	if color == 'green':
		print(Fore.GREEN)

	elif color == 'yellow':
		print(Fore.YELLOW)

	elif color == 'cyan':
		print(Fore.CYAN)

	else:
		print(Fore.WHITE)

def print_completed_dialog():
	print_dialog('-- RESTART GAME? (TYPE Y AND PRESS ENTER TO RESTART OR ANY OTHER AND PRESS ENTER TO EXIT) --')
		
	player_input = input().lower()
	
	if player_input == 'y':
		os.execl(sys.executable, sys.executable, *sys.argv)

	else:
		print('-- THANK YOU FOR PLAYING HANGMAN --')
		sys.exit()
