from abc import abstractmethod

from src.models.UserGameModel import UserGameModel
from src.models.map.Map import Map


class Task:

    def __init__(self):
        self.descr = ""
        self.turns_count = 1
        self.needed_items = list()
        self.buildings = list()
        self.result_items = list()
        self.result_buildings = list()
        self.result_incomes = list()

    def execute(self, user_game_model: UserGameModel):
        pass

    @abstractmethod
    def check_conditions(self, map: Map, user_game_model: UserGameModel): raise NotImplementedError
