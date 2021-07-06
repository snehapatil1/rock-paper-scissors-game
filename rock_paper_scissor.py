import random

def rock_paper_scissor():
	print('Hey buddy. Let\'s play Rock, Paper and Scissors game. For selecting your choice, press ENTER...')
	user = str(input("Type (R) for Rock, (P) for Paper and (S) for Scissor and then ENTER...   ")).lower()

	if user not in ('r', 'p', 's'):
		print('Please enter correct choice.')
		return rock_paper_scissor()

	computer = random.choice(['r', 'p', 's'])

	print(f'Computer\'s choice was {computer.upper()}')
	if user == computer:
		return print('It\'s a Tie.')

	if is_win(user, computer):
		return print('Yayy! You Won...!')

	return print('Oops! You Lost...!')

def is_win(player, opponent):
	# R > S and S > P and P > R
	if (player == 'r' and opponent == 's') \
		or (player == 's' and opponent == 'p') \
		or (player == 'p' and opponent == 'r'):
		return True

	return False

rock_paper_scissor()