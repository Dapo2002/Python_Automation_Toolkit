# A character-frequency analyzer that utilizes 'setdefault' for atomic key initialization and
# 'pprint' for alphabetically sorted, human-readable dictionary output.

import pprint
message = input('Input a message:\n')
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1


pprint.pprint(count)