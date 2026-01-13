# A Monte Carlo simulation that executes 10,000 trials of 100 coin flips to 
# empirically calculate the probability of a 6-event streak of identical outcomes.

import random

numOfStreaks = 0
for experimentNumber in range(10000):
    result = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            result.append('H')
        else:
            result.append('T')

    streak = 1
    for i in range(1, len(result)):
        if result[i] == result[i-1]:
            streak += 1
            if streak == 6:
                numOfStreaks += 1
                break
        elif result[i] != result[i-1]:
            streak = 1
print('The chances of streak of 6 is '+ str(numOfStreaks/10000 * 100) +'%.')