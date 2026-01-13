# A randomized response generator demonstrating the evolution from manual index-
# calculation (randint) to the more abstract and Pythonic 'random.choice' method.

import random

messages = ['It is certain',
            'Yes definitely',
            'Reply hazy, try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
print(random.choice(messages))
