class Vendor:
    def __init__(self, inventory=False):
        self.inventory = inventory if inventory else []
    
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


    # gets best based on condiiton
    def get_best_by_category(self, category):
        items_of_category = []
        for item in self.inventory:
            if item.category == category:
                items_of_category.append({'item': item, 'condition': item.condition})
        if len(items_of_category) == 0:
            return None
        sorted_items = sorted(items_of_category, key=lambda k: k['condition'])
        # returns item from it's place in sorting dict
        return sorted_items[-1]['item']

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        other_items = [] 
        other_best = None      
        # sorts other persons items using same logic as self-sort function
        for item in other.inventory:
            if item.category == my_priority:
                other_items.append({'item': item, 'condition': item.condition})
        other_items.sort(key=lambda k: k['condition'])
        if other_items:
            other_best = other_items[-1]['item']
        if my_best and other_best:
            self.swap_items(other, my_best, other_best)
            return True
        return False