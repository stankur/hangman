from HangmanShared import *


def make_initial_formation(word):
	return '_ ' * len(word)

class GameplayData:
	def __init__(self, word_hint_pair, number_of_chances):
		(word, hint) = word_hint_pair

		self.word = word
		self.hint = hint
		self.chances_left = number_of_chances
		self.player_input = None
		
		self.all_guesses = []
		self.guesses_string = ''
		self.non_letter_inputs = []
		self.correct_guesses = []
		self.hint_request = 0

		self.hangman_formation = make_initial_formation(self.word)
		
		guessed_format = ''

		for letter in self.word:
			guessed_format += letter + ' '
		
		self.guessed_format = guessed_format
