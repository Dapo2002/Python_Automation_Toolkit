# A nested-dictionary aggregator that performs cross-sectional data retrieval by iterating 
# through sub-dictionaries to sum specific item frequencies.

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 3},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for v in guests.values():
        numBrought += v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Pretzels       ' + str(totalBrought(allGuests, 'pretzels')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

print(allGuests['Alice']['pretzels'])