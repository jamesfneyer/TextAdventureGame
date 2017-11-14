inventory_items = []

def get_inventory():
    return inventory_items


def add_item(item):
    inventory_items.append(item)


def remove_item(item):
    inventory_items.pop(item)