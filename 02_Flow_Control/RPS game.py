# A CLI-based Rock Paper Scissors game featuring score tracking, input validation loops, and random AI move generation.

import random
import sys

wins = 0
losses = 0
ties = 0
print('ROCK   PAPER   SCISSORS')
while True:  # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties.')
    while True:  # The player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.')
        move = input('>>> ')
        if move == 'q':
            sys.exit('Thanks for playing! \nFinal score is '+ f'{wins} Wins, {losses} Losses, {ties} Ties.')  # Quit the program
        if move == 'r' or move == 'p' or move == 's':
            break  # Exit the player input loop
        else:
            print('You can only enter r, p, s or q')
    # Display what the player chose
    if move == 'r':
        print('Rock vs ...')
    elif move == 'p':
        print('Paper vs ...')
    elif move == 's':
        print('Scissors vs ...')
    # Display what computer chose
    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('Rock')
    elif computerMove == 2:
        computerMove = 'p'
        print('Paper')
    elif computerMove == 3:
        computerMove = 's'
        print('Scissors')
    # Compare player and computer move
    if move == computerMove:
        print('It\'s a tie!')
        ties += 1
    elif move == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif move == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif move == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif move == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif move == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1
    elif move == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
