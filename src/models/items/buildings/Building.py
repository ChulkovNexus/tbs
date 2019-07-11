from abc import abstractmethod

from src.models.items.BuildingMaterials import Plank
from src.models.items.Item import Item
from src.models.map.Resources import Wood


class Building(Item):

    def __init__(self):
        super().__init__()
        self.religion_influence = 0
        self.war_influence = 0
        self.economic_influence = 0
        self.building_turns_count = 1
        self.allow_to_create_materials = {}
        self.building_resources_needed = {}

    @abstractmethod
    def get_allowed_tasks(self): raise NotImplementedError


class Sawmill(Building):

    def get_allowed_tasks(self):
        return []

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = {Wood: 100}
        self.allow_to_create_materials = {Plank: 1}
