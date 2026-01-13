# inventory.py
# A collection-aggregation script that iterates over key-value pairs to generate
# a formatted report and compute a cumulative sum of item quantities.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("\nTotal number of items: " + str(item_total))


displayInventory(stuff)
