class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        print(self.inventory)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, sought_category):
        matching_category = []
        for item in self.inventory:
            if item.category == sought_category:
                matching_category.append(item)
        return matching_category