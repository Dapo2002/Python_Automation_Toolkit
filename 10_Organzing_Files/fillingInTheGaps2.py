# fillingGaps2.py - Renames numbered files to insert a gap for adding a new file.

import re
import shutil
from pathlib import Path
import pyinputplus

fileNum = {}
p = Path.home()/'practiceTest'
for file in p.glob('spam*'):
    pattern = re.compile(r'\d+')
    mo = pattern.search(file.name).group()
    if mo:
        fileNum[int(mo)] = file
nums = list(fileNum.keys())
nums.sort(reverse=True)
print(nums)
prompt = pyinputplus.inputInt('Which gap in number do you want to put?   ')
if prompt not in nums:
    print('This file number does not exist.')
else:
    for i in nums:
        print(f'Renaming {fileNum[i].name}...')
        shutil.move(fileNum[i], p/f'spam{(i + 1):03}.txt')
        if i == prompt:
            break
print('\nDone!')
