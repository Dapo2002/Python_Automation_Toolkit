# A list-to-prose formatter that implements conditional slicing and string
# joining to convert an array into a grammatically correct serial list.

def listToString(someList):
    if not someList:
        return ''
    elif len(someList) == 1:
        return someList[0]
    else:
        result = ', '.join(someList[:-1])
        result += ' and ' + someList[-1] + '.'
        return result


spamList = []
while True:
    items = input('What is item ' + str(len(spamList) + 1) + '? Press \'Enter\' to input nothing.\n').strip()
    if not items:
        break
    spamList.append(items)

output = listToString(spamList)
if output:
    print(output)
else:
    print("You didn't enter any items.")
