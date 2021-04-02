class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
    
    # add an item to the Vendor's inventory
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
        return item

    # remove an item from the Vendor's inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    # matches items in the vendor's inventory with a sought param
    def get_by_category(self, sought_category):
        matching_category = []
        for item in self.inventory:
            if item.category == sought_category:
                matching_category.append(item)
        return matching_category
    
    # swaps an item with another vendor
    def swap_items(self, recipient, self_item, other_persons_item):
        if self_item in self.inventory and other_persons_item in recipient.inventory:
            recipient.inventory.append(self_item)
            self.inventory.remove(self_item)
            recipient.inventory.remove(other_persons_item)
            self.inventory.append(other_persons_item)
            return True   
        return False
    
    # swaps first item in each vendor's inventory
    def swap_first_item(self, recipient):
        # if both inventories exist, perform swap of first item in list
        if self.inventory and recipient.inventory:
            recipient.inventory.append(self.inventory.pop(0))
            self.inventory.append(recipient.inventory.pop(0))
            return True  
        return False