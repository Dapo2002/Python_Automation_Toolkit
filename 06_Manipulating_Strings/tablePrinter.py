# A tabular data formatter that calculates maximum column-width metadata to perform 
# right-aligned string justification during nested-matrix transposition.

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(someList):
    colWidths = []
    for x in range(len(someList)):
        longestItem = ''
        for y in someList[x]:
            if len(y) > len(longestItem):
                longestItem = y
        colWidths.append(len(longestItem))

    print(colWidths)
    for x in range(len(someList[0])):
        for y in range(len(someList)):
            print(someList[y][x].rjust(colWidths[y]), end=' ')
        print()


printTable(tableData)
