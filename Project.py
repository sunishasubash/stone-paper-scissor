# Please enter: rock, scissors or paper 

import random

possibilities = {'rock': 1, 'scissors': 2, 'paper': 3}

player = input().lower() 

if not (player == 'rock' or player == 'scissors' or player == 'paper'): 

    print( 'Incorrect input. ')

    exit()

num = possibilities.get(player)

computer = random.choice(list(possibilities.keys()))

num_computer = possibilities[computer]

print( 'You: {} - {}  |  Computer: {} - {}'.format(num, player, num_computer, computer))

result = num - num_computer

if result in [-1, 2]:

    print( ' \n You win! ')

elif result in [-2, 1]:

    print( ' \n Computer wins. ')

else:

    print(' \n It\'s a draw. ')
