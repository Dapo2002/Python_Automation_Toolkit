# A file-parsing utility that utilizes regex word-boundary detection to identify 
# and interactively replace grammatical placeholders within an external text 
# document.

import re

file = open('madLibsFile.txt')
readFile = file.read()
file.close()
pattern = re.compile(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b')
matchList = pattern.findall(readFile)
for replace in matchList:
    if replace == 'ADJECTIVE':
        adjective = input('Enter an adjective: ')
    elif replace == 'NOUN':
        noun = input('Enter a noun: ')
    elif replace == 'ADVERB':
        adverb = input('Enter an adverb: ')
    elif replace == 'VERB':
        verb = input('Enter a verb: ')

print(pattern.findall(readFile))
