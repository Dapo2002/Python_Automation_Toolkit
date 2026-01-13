# A dynamic collection-merging script that utilizes the dictionary '.get()' method to
# handle key-initialization and frequency-incrementing for incoming data streams.

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    itemCount = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemCount += v
    return "\nTotal number of items: " + str(itemCount)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
print(displayInventory(inv))
