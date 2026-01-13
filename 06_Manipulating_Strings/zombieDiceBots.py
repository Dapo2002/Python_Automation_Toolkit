# A simulation-based bot framework implementing multiple Object-Oriented
# 'zombie' agents, each utilizing unique heuristic algorithms to manage
# risk and reward in a stochastic game environment.

import random
import zombiedice


# First Zombie: A bot that, after the first roll,
# randomly decides if it will continue or stop
class RandeeTheRisky:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # game state is a dict with info about the current state of the game.
        # you can choose to ignore it in your code

        diceRollResults = zombiedice.roll()  # First roll

        # roll() returns a dictionary with keys 'brains' 'shotgun' and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (colour, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1, 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        # ('green', 'shotgun')]}

        while diceRollResults is not None:
            decision = random.randint(0, 1)
            if decision == 1:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


#  Second bot: A bot that stops rolling after it has rolled two brains
class BrainDrainWayne:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # First roll
        brains = 0
        while diceRollResults is not None:
            if diceRollResults['brains']:
                brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


#  Third bot: A bot that stops rolling after it has rolled two shotguns
class TriggerTim:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # First roll
        shotguns = 0
        while diceRollResults is not None:
            if diceRollResults['shotgun']:
                shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


#  Fourth bot: A bot that initially decides it’ll roll the dice one to four times, but
#  will stop early if it rolls two shotguns
class CautiousCarl:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        rollsToMake = random.randint(1, 4)
        diceRollResults = zombiedice.roll()
        for roll in range(rollsToMake - 1):
            if diceRollResults is None:
                break  # stop if no more dice
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


#  Fifth bot: A bot that stops rolling after it has rolled more shotguns than
# brains
class ParanoidPete:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # First roll
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()


zombies = (RandeeTheRisky(name='RandeeTheRisky'),
           BrainDrainWayne(name='BrainDrainWayne'),
           TriggerTim(name='TriggerTim'),
           CautiousCarl(name='CautiousCarl'),
           ParanoidPete(name='ParanoidPete'))
# Add any other zombie players here


#  Uncomment one of the following lines to run in CLI or Web GUI mode:
#  zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1)
