# A probabilistic simulation utilizing the 'random' module to perform 1,000 
# Bernoulli-like trials, featuring a mid-point execution hook for progress 
# tracking.

import random

head = 0
for i in range(1, 1000):
    if random.randint(0, 2) == 1:
        head += 1
    if i == 500:
        print('Half way there')
print('Number of heads that turned up is ' + str(head))
