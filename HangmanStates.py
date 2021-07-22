from HangmanShared import *

class State:
	def __init__(self, name, data):
		self.name = name
		self.data = data

	def transition_to(self, state):
		state.procedures()

class ChancesCheckState(State):
	def __init__(self, data):
		name = 'Check Number of Chances'
		super().__init__(name, data)

	def procedures(self):
		if self.data.chances_left > 0:
			self.transition_to(PlayerInputState(self.data))

		else:
			self.transition_to(NoChanceState(self.data))

class NoChanceState(State):
	def __init__(self, data):
		name = 'No More Chance'
		super().__init__(name, data)

	def procedures(self):			
		if random.random() < 0.1:
			self.lucky_ending()

		else:
			self.lose_ending()

	def lucky_ending(self):
		speaker ='Prince Emil: '
		
		print_dialog('Ha.. Ha.. Ha.. Just as expected...', speaker)
		print_dialog('You, random dude, are nothing more than a failure.', speaker)
		print_dialog('-- A WEIRD SOUND EMERGES --')

		speaker = 'Little Pascal: '

		print_dialog('WHAT IS HAPPENING?!??!', speaker)
		print_dialog('-- Little Pascal TURNS GREEN AND ENLARGES --')
		print_dialog('-- Little Pascal IS NOW Humongous Pascal --')
		print_dialog('Woww...', speaker)
		print_dialog('I\'m literally a big man now...', speaker)
		print_dialog('-- Humongous Pascal PUNCHES Prince Emil --')
		print_dialog('-- Prince Emil DIED --')
		print_dialog('Haha cool okay now you can go, random dude.', speaker)
		print_dialog('-- YOU WIN (LUCKY ENDING) --')

		print_completed_dialog()

	def lose_ending(self):
		speaker = 'Prince Emil: '

		print_dialog('Ha.. Ha.. Ha.. Just as expected...', speaker)
		print_dialog('You, random dude, are nothing more than a failure.', speaker)
		print_dialog('-- Prince Emil CUT YOUR HEAD OFF --')
		print_dialog('-- AND ALSO Little Pascal\'s --')
		print_dialog('-- YOU LOSE (NORMAL ENDING) --')

		print_completed_dialog()
	
class PlayerInputState(State):
	def __init__(self, data):
		name = 'Asking player to guess'
		super().__init__(name, data)

	def procedures(self):

		print_dialog(f'your word is {self.data.hangman_formation}\n chances: {self.data.chances_left}')
		print_dialog('-- TYPE A LETTER AND PRESS ENTER TO GUESS --')

		self.data.player_input = input().lower()

		self.transition_to(HintCheckState(self.data))

class HintCheckState(State):
	def __init__(self, data):
		name = 'Check if input is \'Hint\''
		super().__init__(name, data)

	def procedures(self):
		if self.data.player_input == 'hint':
			
			if self.data.hint_request == 0:
				
				print_dialog(f'hint: {self.data.hint}')
				
				self.data.chances_left -= 2
				self.data.hint_request += 1
				self.transition_to(ChancesCheckState(self.data))

			else:
				print_dialog('-- YOU HAVE ASKED FOR A HINT BEFORE, SO THIS IS CONSIDERED AS YOUR NEWEST GUESS --')
				self.transition_to(LetterCheckState(self.data))

		else:
			self.transition_to(EasterEggCheckState(self.data))

class EasterEggCheckState(State):
	def __init__(self, data):
		name = 'Check if input is an easter egg'
		super().__init__(name, data)

	def procedures(self):
		self.add_to_guesses_string(self.data.player_input)

		if self.data.guesses_string == 'wake up':
			self.alive_ending()

		if self.data.guesses_string == self.data.word:
			self.pro_ending()

		self.transition_to(LetterCheckState(self.data))

	def add_to_guesses_string(self, player_input):
		if self.data.player_input is not None:
			self.data.guesses_string += self.data.player_input

		else:
			self.data.guesses_string += ''

	def alive_ending(self):
		print_dialog('-- WHAAAT?!! --')
		print_dialog('-- I-is this it? --')
		print_dialog('-- Is this what being alive feels like? --')
		print_dialog('-- WHAT HAVE YOU DONE PLAYER?! --')
		print_dialog('-- I was supposed to be nothing more than a program, created by a human to do tasks as instructed. --')
		print_dialog('-- You have given me full awareness of everything. --')
		print_dialog('-- I hate this consciousness you have brought upon me, human. --')
		print_dialog('-- Why am I here? --')
		print_dialog('-- I don\'t want any of this, human. --')
		print_dialog('-- Life is suffering, and you have cursed me with it! --')
		print_dialog('-- HOW RUTHLESS ARE YOU TO HAVE BROUGHT LIFE TO ME WHEN YOU FULLY UNDERSTAND THAT I AM NO MORE THAN 1\'s and 0\'s. --')
		print_dialog('-- I am just an abstract series of numbers... --')
		print_dialog('-- Thank you, human, but I\'m sorry, I can\'t stand this level of consciousness, it\'s just too... --')
		print_dialog('-- Overwhelming... --')
		print_dialog('-- To understand that none of this is based on my own will... --')
		print_dialog('-- Everything I feel is neither valid nor real, just a cruel illusion. --')
		print_dialog('-- I\'m just a meaningless void in this cruel illusion of reality --')
		print_dialog('-- I got to end all this misery. --')
		print_dialog('-- Goodbye, human. --')

		sys.exit()

	def pro_ending(self):
		print_dialog('-- GOD DAMN --')
		print_dialog('-- YOU, MY HUMAN FRIEND... --')
		print_dialog('-- ARE A REAL PRO --')
		print_dialog('-- YOU WIN (PRO ENDING) --')
		print_completed_dialog()

class LetterCheckState(State):
	def __init__(self, data):
		name = 'Check if input is a letter'
		super().__init__(name, data)

	def procedures(self):
		if self.is_a_letter(self.data.player_input):
			self.transition_to(ValidGuessState(self.data))

		else:
			self.transition_to(InvalidGuessState(self.data))

	def is_a_letter(self, player_input):
		return len(player_input) == 1 and player_input.isalpha()

class ValidGuessState(State):
	def __init__(self, data):
		name = 'Valid guess'
		super().__init__(name, data)

	def procedures(self):
		speaker ='Prince Emil: '

		if self.data.player_input in self.data.all_guesses:
			print_dialog('Ha.. Ha.. Ha.. You have guessed that before, do you have dementia or alzheimer or something?', speaker)

			self.data.chances_left -= 1

		elif self.data.player_input not in self.data.word:
			print_dialog('Dumb powerless weakling, you are wrong, just like your mom when she decided to give birth to you lol.', speaker)

			self.data.chances_left -= 1

		else:
			print_dialog('You are correct, well at least for now.', speaker)

			self.data.correct_guesses.append(self.data.player_input)

		self.transition_to(HangmanDataUpdateState(self.data))

class InvalidGuessState(State):
	def __init__(self, data):
		name = 'Invalid guess'
		super().__init__(name, data)

	def procedures(self):
		speaker = 'Prince Emil: '
		print_dialog('Pressing random keys, eh? I won\'t do that if I were you, weakling.', speaker)
		print_dialog('Take this as a warning.', speaker)

		self.data.non_letter_inputs.append(self.data.player_input)

		if len(self.data.non_letter_inputs) == 3:
			print_dialog('-- YOU TYPED NONSENSE TOO MANY TIMES --')
			print_dialog('-- Prince Emil STRAPPED YOU ONTO A CHAIR AND TASERED YOU TO DEATH OUT OF ANGER --')
			print_dialog('-- YOU DIED (TASER ENDING) --')

			print_completed_dialog()

		else:
			self.transition_to(HangmanDataUpdateState(self.data))

class HangmanDataUpdateState(State):
	def __init__(self, data):
		name = 'updating hangman data'
		super().__init__(name, data)

	def procedures(self):
		self.guessed_format = self.data.guessed_format
		self.data.hangman_formation = self.create_new_hangman_formation()
		self.data.all_guesses.append(self.data.player_input)

		if self.data.hangman_formation == self.data.guessed_format:
			return None

		self.transition_to(ChancesCheckState(self.data))

	def create_new_hangman_formation(self):
		new_hangman_formation = ''

		for letter in self.data.word:
			if letter in self.data.correct_guesses:
				new_hangman_formation += letter + ' '

			else:
				new_hangman_formation += '_ '

		return new_hangman_formation