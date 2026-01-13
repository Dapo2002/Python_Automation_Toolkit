# A program that walks through a folder and selectively deletes files from greater than 100MB

import os
from pathlib import Path

p = Path(r'C:\Users\User\Desktop\DAPO')
for x, y, z in os.walk(p):
    for filename in y:
        fileAbsPath = os.path.join(x, filename)
        fileSize = os.path.getsize(fileAbsPath)
        if fileSize > (100 * 1024 * 1024):
            print(fileAbsPath)
print('\nDone!')
