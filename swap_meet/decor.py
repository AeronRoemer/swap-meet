class Decor:
    def __init__(self, condition=None):
        self.category = "Decor"
        self.condition = condition

    def condition_description(self):
        return str(self.condition)

    def __str__(self):
        return "Something to decorate your space."