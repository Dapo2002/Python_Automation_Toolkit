# A numeric guessing game using a 'for' loop to limit the player to exactly 6 attempts.

import random

print('I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)
for guessTaken in range (1, 7):
    guess = int(input('Take a guess: '))
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses.')
else:
    print('Nope, the number i was thinking of is ' + str(secretNumber) + '.')
