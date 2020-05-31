# Class model for a meal planner


class Meal ():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = {'ingredients' : ingredients}

    def __str__(self):
        return f"Aby wykonać {self.name}, musisz kupić {self.ingredients}"


class Dinner(Meal):
    def __init__(self, name, ingredients):
        super().__init__(name, ingredients)
        self.tags = ['dinner', 'lunch']


class Non_dinner(Meal):
    def __init__(self, name, ingredients):
        super().__init__(name, ingredients)
        self.tags = ['breakfast', 'brunch', 'supper']


class Snack (Meal):
    def __init__(self, name, ingredients):
        super().__init__(name, ingredients)
        self.tags = ['snack', 'appetizer', 'starter', 'between meals']


class Shopping_list():
    def __init__(self):
        self.list = []