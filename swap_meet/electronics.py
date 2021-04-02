class Electronics:
    def __init__(self,condition=None):
        self.category = "Electronics"
        self.condition = condition
        
    def condition_description(self):
        return str(self.condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."