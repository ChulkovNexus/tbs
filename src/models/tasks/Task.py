from abc import abstractmethod

from src.models.person.Person import Person
from src.models.map.Map import Map


class Task:

    def __init__(self):
        self.descr = ""
        self.game_model = None
        self.turns_count = 1
        #todo менять turns count от персоонажа который исполняет таск
        self.skill_for_calculating_turns = None
        self.needed_items = list()
        self.buildings = list()
        self.result_items = list()
        self.result_buildings = list()
        self.result_incomes = list()

    def execute(self, user_game_model, person: Person):
        self.game_model = user_game_model

    @abstractmethod
    def check_conditions(self, map: Map, user_game_model, person: Person): raise NotImplementedError

    @abstractmethod
    def get_resources_for_consume(self): raise NotImplementedError

    def on_append_to_task_schedule(self):
        pass

    def on_remove_from_task_schedule(self):
        pass
