from HangmanShared import *
import HangmanInitialData
import HangmanStates

speaker = 'Unknown: '

print_dialog('-- WELCOME TO HANGMAN --')
print_dialog('Hello random guy, welcome to the Supreme Court of Brilliantland!', speaker)
print_dialog('Sorry for abducting you from your bed, but don\'t panic, I\'ll explain everything.', speaker)
print_dialog('--> :) <--')
print_dialog('That right there is little Pascal.', speaker)
print_dialog('He spilled his ice cream in front King Campbell\'s castle.', speaker)
print_dialog('Our almighty King slipped on that ice cream, broke his bone and died.', speaker)
print_dialog('We don\'t really know whether to let little Pascal live or execute him.', speaker)
print_dialog('Don\'t panic, but his life actually depends on you right now lol.', speaker)
print_dialog('I\'ll give you a word to guess.', speaker)
print_dialog('Guess the word right and little Pascal lives. Otherwise, he\'s no more.', speaker)
print_dialog('Oh, and I\'ll kill you too if you fail to guess lol.', speaker)
print_dialog('You have 5 chances, each time you make a wrong move, I take 1 away.', speaker)
print_dialog('When you run out of chances, you will also run out of life lol.', speaker)
print_dialog('Cuz I will kill you and that lil Pascal bastard!', speaker)
print_dialog('Pick and type a category from the following: BC People Name, Body Part, Fruit.', speaker)
print_dialog('-- PLEASE TYPE YOUR CHOICE AND PRESS ENTER TO PROCEED --')

#this is trying to receive a valid input of the player's category of choice
player_input = input().lower()

request_times = 0

while player_input not in hangman_words:
	print_dialog('Ha..  Ha.. Ha.. Think again before doing that, you\'ve got nerves doing that, weaklling!', speaker)
	print_dialog('-- PLEASE RETYPE A VALID CATEGORY --')

	request_times += 1
	player_input = input().lower()

	if request_times == 2 and player_input == 'grab':
		print_dialog('-- Unknown was about to cut your head off, but somehow you managed to grab his sword --')
		print_dialog('-- you pull the sword from his hand and use it to stab him to death --')
		print_dialog('-- YOU WIN (STAB ENDING) --')

		print_completed_dialog()

	if request_times == 3:
		print_dialog('-- YOU TYPED NONSENSE TOO MANY TIMES --')
		print_dialog('-- Unknown REACHED HIS SWORD AND CUT YOUR HEAD OFF OUT OF ANGER AND ANNOYANCE --')
		print_dialog('-- YOU DIED (ANNOYING PLAYER ENDING) --')

		print_completed_dialog()

print_dialog('Oh, how rude! I haven\'t introduced myself.', speaker)
print_dialog('I am Prince Emil Yakun, the only son of King Campbell, but you can call me King Yakun as I will be crowned in no time anyway lol.', speaker)

speaker = 'Prince Emil: '

print_dialog('Anyway let\'s start this little game, shall we?', speaker)
print_dialog('-- PLEASE GUESS ONE LETTER AT A TIME --')
print_dialog('-- YOU CAN ASK FOR A HINT 1 TIME AT THE COST OF 2 CHANCES BY TYPING HINT AND PRESSING ENTER --')

(word, hint) = random.choice(hangman_words[player_input])

initial_chances = 5

Gameplay_Data = HangmanInitialData.GameplayData((word, hint), initial_chances)

#This leads to the initial state of the game. The states will then transition automatically to other stages of the game depending on the player's  inputs
#All the states available in the game are in HangmanStates.py
HangmanStates.ChancesCheckState(Gameplay_Data).procedures()

#The code escapes the state machine only when the player has correctly guessed the eword without running out of chances
#This is the normal winning ending
print_dialog('Nice... You turn out to be not that dumb, eh...', speaker)
print_dialog('But too bad you\'re not intelligent enough to understand that I don\'t care about this little game lol.', speaker)
print_dialog('I\'ll still kill you, a random useless dude, and that stupid little Pascal.', speaker)
print_dialog('Ha.. Ha.. Ha.. Life is funny ain\'t it, my friend...', speaker)
print_dialog('You only had it to get killed by me, a powerful royalty.', speaker)
print_dialog('-- Prince Emil REACHES FOR HIS SWORD... --')
print_dialog('-- THE LIGHTS BLINK ON AND OFF --')
print_dialog('What the hell?!', speaker)

speaker = 'Spirit: '

print_dialog('-- BLOOD STARTS TO RUSH OUT OF Prince Emil\'s MOUTH --')
print_dialog('-- Prince Emil DIED --')
print_dialog('My name is Fiona and I am here to protect the sacred Brilliantland...', speaker)

speaker = 'Ghost Fiona: '

print_dialog('You my friend, have proven yourself worthy! I am truly amazed by your level of brilliance!', speaker)
print_dialog('little Pascal right here is the only true son of King Campbell.', speaker)
print_dialog('Prince Emil is never a prince, he\'s nothing more than a physically fluid evil witch. He\'s a monster...' , speaker)
print_dialog('Long ago, he kidnapped the baby of King Campbell, and abandoned the baby near the Brilliant river.', speaker)
print_dialog('What this dumb witch doesn\'t know is that the baby was saved and adopted by a kind and loving local fisherman named Elbert.', speaker)
print_dialog('Elbert the kind fisherman took care of this baby and named him after the language of Brilliantland, Pascal.', speaker)
print_dialog('Wicked Emil has been playing along for quite a while now, pretending to be King Campbell\'s true son', speaker)
print_dialog('King Campbell was about to meet little Pascal and Emil the wicked witch was worried that the king might find out.', speaker)
print_dialog('So, he decided to kill the king using his spells and frame little Pascal to be the culprit.', speaker)
print_dialog('Little Pascal is actually the next monarch in the royalty line of Brilliantland!', speaker)
print_dialog('And now, the whole sacred Brilliantland shall bow to the new king, King Pascal!', speaker)

speaker = 'King Pascal: '

print_dialog('Nani?? I was about to get killed and suddenly I\'m a new king lol ok whatever.', speaker)
print_dialog('I\'m also only 10 but who\'d be dumb enough to not want to be king lol.', speaker)
print_dialog('Anyway, thanks for saving me, dude hehe.', speaker)

speaker = 'Ghost Fiona: '

print_dialog('Due to your crazy skill, my friend, I bless you with an internship offer at the largest tech company in Brilliantland.', speaker)
print_dialog('-- YOU WIN (HAPPY ENDING) --')

print_completed_dialog()