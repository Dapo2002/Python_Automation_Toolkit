# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import re
import shutil
import os

#  Create a regex that matches files with the American date format
datePattern = re.compile(r'''
    ^(.*?)
    ((?:0?[1-9]|1[0-2])[-/])
    ((?:0?[1-9]|[12]\d|3[01])[-/])
    ((?:19|20)\d\d)
    (.*?)$''', re.VERBOSE)


#  Loop over the files in the working directory
for amerFilename in os.listdir('./renameDates_testFolder'):
    mo = datePattern.search(amerFilename)
    #  Skip files without a date
    if mo is None:
        continue
    #  Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)
    #  Form the european style filename
    euroFilename = beforePart + dayPart + monthPart + yearPart + afterPart
    #  Get the full absolute file paths
    absWorkingDir = os.path.join('./renameDates_testFolder')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, 'renamed', euroFilename)
    #  Rename the files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.copy(amerFilename, euroFilename)
