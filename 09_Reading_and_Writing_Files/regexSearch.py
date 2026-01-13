# A file-system search utility that utilizes 'pathlib' globbing and regex to 
# perform line-by-line pattern matching across all text documents in the current 
# directory.

import re
from pathlib import Path

p = Path.cwd()
patternPrompt = input('Enter the pattern you want to find:\n')
pattern = re.compile(patternPrompt)
dirContent = list(p.glob('*.txt'))
matchFound = False
for i, file in enumerate(dirContent):
    with open(file) as dirFile:
        fileContent = dirFile.readlines()
        for j in range(len(fileContent)):
            match = pattern.findall(fileContent[j])
            if match:
                matchFound = True
                print(f'Match found >>> {match}. Line {j + 1} of file {file.name}\n')
if not dirContent:
    print('No text files in this folder')
elif not matchFound:
    print('Match not found')
