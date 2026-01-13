# A numeric guessing game using a 'while' loop and state variables to track game progress and exit conditions.

import random

print('I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)
guessTaken = 0
guess = 0
while guess != secretNumber and guessTaken < 6:
    guess = int(input('Take a guess: '))
    guessTaken += 1
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
