#  A program that walks through a folder and selectively copies .jpg and .pdf files from src to dst

import os
import shutil
from pathlib import Path

p = Path(r'C:\Users\User\Desktop\DAPO')
dstFolder = Path.home()/'selectiveCopy_test'
for x, y, z in os.walk(p):
    for filename in z:
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            os.makedirs(dstFolder, exist_ok=True)
            print(f'Copying {filename}...')
            shutil.copy(Path(x)/filename, dstFolder)
print('\nDone!')
