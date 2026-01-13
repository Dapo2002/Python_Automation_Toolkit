# A regex-driven date extractor and validator that utilizes verbose pattern matching
# and leap-year logic to audit clipboard data for Gregorian calendar compliance.

import re
import pyperclip

date = pyperclip.paste()
dateFormat = re.compile(r'''(?:^|\D)(
    (0?[1-9]|[12][0-9]|3[01])/   #  day
    (0?[1-9]|1[0-2])/            #  month
    (1[0-9]{3}|2[0-9]{3})          #  year
    (?:$|\D))''', re.VERBOSE)

result = []


def is_leap(years):
    return (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)


for dates in dateFormat.findall(date):
    fullDate = dates[0]
    day = int(dates[1])
    month = int(dates[2])
    year = int(dates[3])

    _30DaysMonth = [4, 6, 9, 11]
    if (month in _30DaysMonth and day > 30) or \
            (is_leap(year) and month == 2 and day > 29) or \
            (not is_leap(year) and month == 2 and day > 28):
        result.append(fullDate + ' >> Invalid Date!')
    else:
        result.append(fullDate + ' >> Valid Date!')

print('\n'.join(result))
pyperclip.copy('\n'.join(result))
