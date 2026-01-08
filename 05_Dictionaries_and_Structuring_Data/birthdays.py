# A dynamic dictionary-based database that utilizes key-value mapping for O(1) 
# retrieval and runtime data persistence.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    name = input('Enter a name :\n')
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name + '.')
    else:
        print('I do not have birthday data for ' + name + '.\nWhat is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday data updated.')
