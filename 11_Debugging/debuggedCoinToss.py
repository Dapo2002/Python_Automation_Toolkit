#  debuggedCoinToss -- FIXED
# A refined interactive game utilizing input validation loops and boolean logic 
# to synchronize integer-based randomization with string-based user guesses.

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Enter heads or tails:')
        guess = input()
    if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
