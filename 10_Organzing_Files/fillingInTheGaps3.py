# fillingGaps2.py - Create numbered files to close numbering gaps.

from pathlib import Path

p = Path.home()/'spamFolder'
m = p.glob('*')
fileInt = []
for i, files in enumerate(m):
    fileNum = int(files.name[4:-4])
    fileInt.append(fileNum)
fileInt.sort()

MFileInt = []
for j, num in enumerate(fileInt):
    fileIntDiff = 0
    if (j + 1) < len(fileInt):
        fileIntDiff = fileInt[j + 1] - fileInt[j]
    if fileIntDiff > 1:
        for f in range(fileIntDiff-1):
            MFileInt.append(fileInt[j]+(f + 1))
print(fileInt)
fileInt.extend(MFileInt)
fileInt.sort()
print(MFileInt)
print(fileInt)
for file in MFileInt:
    open(Path.home()/f'spamFolder2/spam{file:03}.txt', 'w').write('Bacon is a vegetable!')
    print(f'Creating file {file}...')
print('\nDone!')
