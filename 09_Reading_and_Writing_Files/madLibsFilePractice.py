# An interactive template-filling engine that utilizes iterative regex 
# substitution and the 'with' context manager to perform non-destructive file 
# transformations.

import re

textFile = open('madLibsTextFile')
readTextFile = textFile.read()
textFile.close()
pattern = re.compile(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b')
match = pattern.findall(readTextFile)
for word in match:
    replace = ''
    if word == 'ADJECTIVE':
        replace = input('Enter an adjective: ')
    elif word == 'NOUN':
        replace = input('Enter a noun: ')
    elif word == 'ADVERB':
        replace = input('Enter an adverb: ')
    elif word == 'VERB':
        replace = input('Enter a verb: ')
    readTextFile = pattern.sub(replace, readTextFile, count=1)
print(readTextFile)
with open('madLibsTextFile(Ans)', 'w') as newReadTextFile:
    newReadTextFile.write(readTextFile)
