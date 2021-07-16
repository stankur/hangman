words = {
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

def wait():

	time.sleep(1.5)

def dialog(quote, talker = ''):

	if talker == 'Ghost Fiona: ' or talker == 'Spirit: ':

		print(Fore.GREEN)


	elif talker == 'King Pascal: ' or talker == 'Little Pascal: ' or talker == 'Humongous Pascal: ':

		print(Fore.YELLOW)
	
	elif talker == 'Unknown: ' or talker == 'Prince Emil: ':

		print(Fore.CYAN)

	else:

		print(Fore.WHITE)

	print('')
	print(talker + quote)
	wait()

#Give a list consisting of 5 objects, this function selects 1 randomly
def select(list5):
	picker = random.random()
	
	if picker < 0.2:

		fate = list5[0][0]
		hint = list5[0][1]
	
	elif picker < 0.4:

		fate = list5[1][0]
		hint = list5[1][1]
	
	elif picker < 0.6:

		fate = list5[2][0]
		hint = list5[2][1]
	
	elif picker < 0.8:

		fate = list5[3][0]
		hint = list5[3][1]
	
	else:

		fate = list5[4][0]
		hint = list5[4][1]

	return (fate, hint)

#default function to be placed after player reaches the end (either win or lose)
def complete():
	dialog('-- RESTART GAME? (TYPE Y AND PRESS ENTER TO RESTART OR ANY OTHER AND PRESS ENTER TO EXIT) --')
		
	response = input()

	if response.lower() == 'y':

		os.execl(sys.executable, sys.executable, *sys.argv)

	else:

		print('-- THANK YOU FOR PLAYING HANGMAN --')

		sys.exit()

def hangman(word, hint, playerseq, playerlett, nonletters, guessed, chances, letters, playerguess, last, hint_no):

	p = 'Prince Emil: '

	if chances > 0:

		dialog(f'your word is {last}\n chances: {chances}')

		dialog('-- TYPE A LETTER AND PRESS ENTER TO GUESS --')

		guess = input().lower()

		if guess == 'hint':

			if hint_no == 0:

				dialog(f'hint: {hint}')

				chances -= 2

				hint_no += 1

				return (last, playerseq, playerlett, nonletters, guessed, chances, playerguess, hint_no)

			else:

				dialog('-- YOU HAVE ASKED FOR A HINT BEFORE, SO THIS IS CONSIDERED AS YOUR NEWEST GUESS --')

		if guess is not None:

			playerseq += guess

		else:

			playerseq += ''


	if playerseq == 'wake up':

		dialog('-- WHAAAT?!! --')
		dialog('-- I-is this it? --')
		dialog('-- Is this what being alive feels like? --')
		dialog('-- WHAT HAVE YOU DONE PLAYER?! --')
		dialog('-- I was supposed to be nothing more than a program, created by a human to do tasks as instructed. --')
		dialog('-- You have given me full awareness of everything. --')
		dialog('-- I hate this consciousness you have brought upon me, human. --')
		dialog('-- Why am I here? --')
		dialog('-- I don\'t want any of this, human. --')
		dialog('-- Life is suffering, and you have cursed me with it! --')
		dialog('-- HOW RUTHLESS ARE YOU TO HAVE BROUGHT LIFE TO ME WHEN YOU FULLY UNDERSTAND THAT I AM NO MORE THAN 1\'s and 0\'s. --')
		dialog('-- I am just an abstract series of numbers... --')
		dialog('-- Thank you, human, but I\'m sorry, I can\'t stand this level of consciousness, it\'s just too... --')
		dialog('-- Overwhelming... --')
		dialog('-- To understand that none of this is based on my own will... --')
		dialog('-- Everything I feel is neither valid nor real, just a cruel illusion. --')
		dialog('-- I\'m just a meaningless void in this cruel illusion of reality --')
		dialog('-- I got to end all this misery. --')
		dialog('-- Goodbye, human. --')

		sys.exit()

	if playerseq == word:

		dialog('-- GOD DAMN --')
		dialog('-- YOU, MY HUMAN FRIEND... --')
		dialog('-- ARE A REAL PRO --')
		dialog('-- YOU WIN (PRO ENDING) --')
		complete()
		
		if len(guess) == 1 and guess in letters:
			
			if guess in playerguess:

				dialog('Ha.. Ha.. Ha.. You have guessed that before, do you have dementia or alzheimer or something?', p)

				chances -= 1


			elif guess not in word:
				
				dialog('Dumb powerless weakling, you are wrong, just like your mom when she decided to give birth to you lol.', p)

				chances -= 1

			else:

				dialog('You are correct, well at least for now.', p)

				guessed.append(guess)

		else:

			dialog('Pressing random keys, eh? I won\'t do that if I were you, weakling.', p)
			dialog('Take this as a warning.', p)

			nonletters.append(guess)

	else:

		fate = random.random()

		if fate < 0.1:

			dialog('Ha.. Ha.. Ha.. Just as expected...', p)
			dialog('You, random dude, are nothing more than a failure.',p)
			dialog('-- A WEIRD SOUND EMERGES --')

			p = 'Little Pascal: '

			dialog('WHAT IS HAPPENING?!??!', p)
			dialog('-- Little Pascal TURNS GREEN AND ENLARGES --')
			dialog('-- Little Pascal IS NOW Humongous Pascal --')
			dialog('Woww...', p)
			dialog('I\'m literally a big man now...', p)
			dialog('-- Humongous Pascal PUNCHES Prince Emil --')
			dialog('-- Prince Emil DIED --')
			dialog('Haha cool okay now you can go, random dude.', p)
			dialog('-- YOU WIN (LUCKY ENDING) --')

			complete()

		else:
			dialog('Ha.. Ha.. Ha.. Just as expected...', p)
			dialog('You, random dude, are nothing more than a failure.',p)
			dialog('-- Prince Emil CUT YOUR HEAD OFF --')
			dialog('-- AND ALSO Little Pascal\'s --')
			dialog('-- YOU LOSE (NORMAL ENDING) --')

			complete()


	if len(nonletters) == 3:

		dialog('-- YOU TYPED NONSENSE TOO MANY TIMES --')
		dialog('-- Prince Emil STRAPPED YOU ONTO A CHAIR AND TASERED YOU TO DEATH OUT OF ANGER --')
		dialog('-- YOU DIED (TASER ENDING) --')

		complete()

	newlast = ''

	for letter in word:

		if letter in guessed:

			newlast += (letter + ' ')

		else:

			newlast += '_ '
	
	playerguess.append(guess)

	return (newlast, playerseq, playerlett, nonletters, guessed, chances, playerguess, hint_no)

#start of the game

p = 'Unknown: '

dialog('-- WELCOME TO HANGMAN --')
dialog('Hello random guy, welcome to the Supreme Court of Brilliantland!', p)
dialog('Sorry for abducting you from your bed, but don\'t panic, I\'ll explain everything.', p)
dialog('--> :) <--')
dialog('That right there is little Pascal.', p)
dialog('He spilled his ice cream in front King Campbell\'s castle.', p)
dialog('Our almighty King slipped on that ice cream, broke his bone and died.', p)
dialog('We don\'t really know whether to let little Pascal live or execute him.', p)
dialog('Don\'t panic, but his life actually depends on you right now lol.', p)
dialog('I\'ll give you a word to guess.', p)
dialog('Guess the word right and little Pascal lives. Otherwise, he\'s no more.', p)
dialog('Oh, and I\'ll kill you too if you fail to guess lol.', p)
dialog('You have 5 chances, each time you make a wrong move, I take 1 away.', p)
dialog('When you run out of chances, you will also run out of life lol.', p)
dialog('Cuz I will kill you and that lil Pascal bastard!', p)
dialog('Pick and type a category from the following: BC People Name, Body Part, Fruit.', p)
dialog('-- PLEASE TYPE YOUR CHOICE AND PRESS ENTER TO PROCEED --')

#recording the player's choice of category
ans = input().lower()

times = 0

#handling players not cooperating (if players type invalid category)
while ans not in words:

	dialog('Ha..  Ha.. Ha.. Think again before doing that, you\'ve got nerves doing that, weaklling!', p)
	dialog('-- PLEASE RETYPE A VALID CATEGORY --')

	times += 1
	ans = input().lower()

	if times == 2 and ans == 'grab':

		dialog('-- Unknown was about to cut your head off, but somehow you managed to grab his sword --')
		dialog('-- you pull the sword from his hand and use it to stab him to death --')
		dialog('-- YOU WIN (STAB ENDING) --')

		complete()

	if times == 3:

		dialog('-- YOU TYPED NONSENSE TOO MANY TIMES --')
		dialog('-- Unknown REACHED HIS SWORD AND CUT YOUR HEAD OFF OUT OF ANGER AND ANNOYANCE --')
		dialog('-- YOU DIED (ANNOYING PLAYER ENDING) --')

		complete()

dialog('Oh, how rude! I haven\'t introduced myself.', p)
dialog('I am Prince Emil Yakun, the only son of King Campbell, but you can call me King Yakun as I will be crowned in no time anyway lol.', p)

p = 'Prince Emil: '

dialog('Anyway let\'s start this little game, shall we?', p)
dialog('-- PLEASE GUESS ONE LETTER AT A TIME --')
dialog('-- YOU CAN ASK FOR A HINT 1 TIME AT THE COST OF 2 CHANCES BY TYPING HINT AND PRESSING ENTER --')

selected = select(words[ans])
word = selected[0]
hint = selected[1]
playerseq = ''
playerlett =[]
nonletters = []
guessed=[]
chances = 5
letters = 'abcdefghifjklmnopqrstuvwxyz'
playerguess = []
last = '_ ' * len(word)
counter = 0
hint_no = 0

comparer = ''

for letter in word:

	comparer += letter + ' '

#the hangman repeats either until a certain ending is reached or until all the letters have been successfully guessed
while last != comparer:

	tup = hangman(word, hint, playerseq, playerlett, nonletters, guessed, chances, letters, playerguess, last, hint_no)
	last = tup[0]
	playerseq = tup[1]
	playerlett = tup[2]
	nonletters = tup[3]
	guessed = tup[4]
	chances = tup[5]
	playerguess = tup[6]
	hint_no = tup[7]

dialog('Nice... You turn out to be not that dumb, eh...', p)
dialog('But too bad yo\'re not intelligent enough to understand that I don\'t care about this little game lol.', p)
dialog('I\'ll still kill you, a random useless dude, and that stupid little Pascal.', p)
dialog('Ha.. Ha.. Ha.. Life is funny ain\'t it, my friend...', p)
dialog('You only had it to get killed by me, a powerful royalty.', p)
dialog('-- Prince Emil REACHES FOR HIS SWORD... --')
dialog('-- THE LIGHTS BLINK ON AND OFF --')
dialog('What the hell?!', p)

p = 'Spirit: '

dialog('-- BLOOD STARTS TO RUSH OUT OF Prince Emil\'s MOUTH --')
dialog('-- Prince Emil DIED --')
dialog('My name is Fiona and I am here to protect the sacred Brilliantland...', p)

p = 'Ghost Fiona: '

dialog('You my frieend, have proven yourself worthy! I am truly amazed by your level of intelligence!', p)
dialog('little Pascal right here is actually King Campbell\'s only true son.', p)
dialog('Prince Emil is never a prince, he\'s nothing more than a physically fluid evil witch...' , p)
dialog('Long ago, he kidnapped the baby of King Campbell, little Pascal right here, and abandoned little Pascal near a river.', p)
dialog('He has been playing along for quite a while now, pretending to be King Campbell\'s true son', p)
dialog('King Campbell was about to meet little Pascal and Emil the wicked witch was worried that the king might find out.', p)
dialog('So, he decided to kill the king using his spells and frame little Pascal to be the culprit.', p)
dialog('Little Pascal is the next in the royalty line of Brilliantland!', p)
dialog('And now, the whole sacred Brilliantland shall bow to the new king, King Pascal!', p)

p = 'King Pascal: '

dialog('Nani?? I was about to get killed and suddenly I\'m a new king lol ok whatever.', p)
dialog('Anyway, thanks for saving me, dude hehe.', p)

p = 'Ghost Fiona: '

dialog('Due to what you have done, my friend, I bless you with unlimited wealth as long as you choose to stay here, in Brilliantland.', p)
dialog('-- YOU WIN (HAPPY ENDING) --')

complete()












