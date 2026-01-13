# A dynamic sandwich-ordering system utilizing 'inputMenu' for selection-driven 
# data entry and 'inputInt' for quantitative constraints.

import pyinputplus as pyip
import random

order = []
print('Let\'s make your sandwich>>>\n\n')
breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Which type'
                                                                   ' of bread do you want:\n',
                           numbered=True)
order.append(breadType)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Protein?:\n', numbered=True)
order.append(protein)

if pyip.inputYesNo(prompt='Do you want cheese?\n') == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Cheese type?:\n', numbered=True)
    order.append(cheese)
toppings = ['mayo', 'mustard', 'lettuce', 'tomato']

for i in toppings:
    ask = pyip.inputYesNo(prompt='Do you want ' + i + '?\n')
    if ask == 'yes':
        order.append(i)

numberOfSandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n', min=1)
totalPrice = 0

print()
for i in order:
    price = random.randint(1000, 10000)
    print(f'{i:<16}>>> ${price:<7}')
    totalPrice += price
print(f'\nTotal Cost >>> ${totalPrice}')
totalPrice *= numberOfSandwiches
print(f'Total price for {numberOfSandwiches} sandwiches>>> ${totalPrice}')
