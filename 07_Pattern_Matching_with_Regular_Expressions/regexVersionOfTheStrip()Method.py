# A custom string-sanitization utility that replicates the 'strip' method logic 
# using regex substitution to prune leading and trailing character sets.

import re

leading = re.compile(r'^(\s+)')
trailing = re.compile(r'(\s+)$')


def strip(someString, stripper):
    if not stripper:
        someString = leading.sub('', someString)
        someString = trailing.sub('', someString)
    else:
        customLeading = re.compile('^['+stripper+']+')
        customTrailing = re.compile('['+stripper+']+$')
        someString = customLeading.sub('', someString)
        someString = customTrailing.sub('', someString)
    return someString


string, stripChar = input('Enter a string to strip:\n'), input(
    'Enter character to strip (Press "Enter" if just whitespace)\n')
print(strip(string, stripChar))
