from src.models.items.ItemsStack import ItemsStack


class UserGameModel:

    def __init__(self):
        self.user_id = 0
        self.game_id = 0
        self.pos_x = 0
        self.pos_y = 0
        self.persons = list()
        self.items = ItemsStack()
        self.military_income_value = list()
        self.cult_income_value = list()
        self.religion_income_value = list()
