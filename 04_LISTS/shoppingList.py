# An inventory-recall script utilizing 'enumerate' for indexed output and 'set' 
# comparison to validate collection equivalence as a loop termination condition.

supplies = ['fan', 'remote', 'phone', 'mirror', 'plates']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' of supplies is: ' + item)

mentioned = []
while True:
    name = input('name: ')
    if name not in supplies:
        print('I didn\'t buy ' + name)
    elif name in mentioned:
        print('You already mentioned '+name+'.')
    else:
        print('I bought ' + name+', what else did i buy?')
        mentioned.append(name)
    if set(mentioned) == set(supplies):
        break
print('Good memory.')