from abc import abstractmethod

from src.models.items.Item import Item


class Building(Item):

    @abstractmethod
    def get_allowed_tasks(self): raise NotImplementedError

    def get_religion_influence(self):
        return 0

    def get_war_influence(self):
        return 0

    def get_economic_influence(self):
        return 0
