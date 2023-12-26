import random
import os
import shutil
import time

COLOR = '\033[0m'
RED_COLOR = '\033[91m'
GREEN_COLOR = '\033[92m'
YELLOW_COLOR = '\033[93m'
RESET_COLOR = '\033[0m'


spells = [
    '0COLD SNAP',
    '1GHOST WALK',
    '2TORNADO',
    '3E.M.P',
    '4ALACRITY',
    '5CHAOS METEOR',
    '6SUN STRIKE',
    '7FORGE SPIRIT',
    '8ICE WALL',
    '9DEAFENING BLAST',
]

keys = [
    '0qqq',
    '1qqw',
    '2wwq',
    '3www',
    '4wwe',
    '5eew',
    '6eee',
    '7eeq',
    '8qqe',
    '9qwe',
]

score = 0
maxscore = 0
columns = shutil.get_terminal_size().columns
input_time = 0
best_input_time = 0

def currentscore(columns):
	if score < 10:
		if score < maxscore:
			COLOR = RED_COLOR
		if score > maxscore:
			COLOR = GREEN_COLOR
		if score > (maxscore // 2) and score < maxscore:
			COLOR = YELLOW_COLOR
		if score == maxscore:
			COLOR = GREEN_COLOR
		print('\n\n\n\n')
		print(f'        SCORE:      {COLOR}{score}{RESET_COLOR}'.center(columns))
		print(f'    MAXSCORE:   {maxscore}{RESET_COLOR}'.center(columns))
		print(f'       LAST TIME:  {input_time:.2f}{RESET_COLOR}'.center(columns))
		print(f'       BEST TIME:  {best_input_time:.2f}{RESET_COLOR}'.center(columns))
		print('\n\n\n\n')
	if score >= 10:
		if score < maxscore:
			COLOR = RED_COLOR
		if score > maxscore:
			COLOR = GREEN_COLOR
		if score > (maxscore // 2) and score < maxscore:
			COLOR = YELLOW_COLOR
		if score == maxscore:
			COLOR = GREEN_COLOR
		print('\n\n\n\n')
		print(f'         SCORE:      {COLOR}{score}{RESET_COLOR}'.center(columns))
		print(f'    MAXSCORE:   {maxscore}{RESET_COLOR}'.center(columns))
		print(f'       LAST TIME:  {input_time:.2f}{RESET_COLOR}'.center(columns))
		print(f'       BEST TIME:  {best_input_time:.2f}{RESET_COLOR}'.center(columns))
		print('\n\n\n\n')
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    currentscore(columns)
    randspell = random.choice(spells)
    randspellnum = int(randspell[0:1])
    randkeys = keys[randspellnum]
    print(f'{randspell[1::].center(columns)}{RESET_COLOR}', '\n\n\n\n\n\n\n\n\n\n\n')
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    if user_input == randkeys[1::]:
        score += 1
        if maxscore < score:
            maxscore = score
        input_time = end_time - start_time
        if best_input_time > input_time or best_input_time == 0:
            best_input_time = input_time
    else:
        score = 0