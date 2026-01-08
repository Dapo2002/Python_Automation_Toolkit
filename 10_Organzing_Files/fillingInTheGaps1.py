# fillingGaps1.py - Finds files with a given prefix and renames them to close numbering gaps.

import re
import shutil
from pathlib import Path

numList = {}
p = Path.home()/'spamFolder'
for i in p.glob('spam*'):
    pattern = re.compile(r'\d+')
    mo = pattern.search(i.name).group()
    if mo:
        numList[int(mo)] = i
nums = list(numList.keys())
nums.sort()
print(nums)
expected = 1
for i in nums:
    if i != expected:
        shutil.move(p/numList[i], p/f'spam{expected:03}.txt')
    expected += 1
