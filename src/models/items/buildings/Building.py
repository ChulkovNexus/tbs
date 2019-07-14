from abc import abstractmethod

from src.models.items.BuildingMaterials import Plank
from src.models.items.Item import Item
from src.models.map.Resources import Wood, Metal, Stone


class Building(Item):

    def __init__(self):
        super().__init__()
        self.religion_influence = 0
        self.war_influence = 0
        self.economic_influence = 0
        self.building_turns_count = 1
        self.allow_to_create_materials = {}
        self.allow_to_create_buildings = []
        self.necessary_buildings = []
        self.building_resources_needed = [{}]

    @abstractmethod
    def get_allowed_tasks(self): raise NotImplementedError

    def __repr__(self):
        return f"{type(self).__name__}"


class HiddenPost(Building):

    def get_allowed_tasks(self):
        return []

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 1
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 200}]
        self.allow_to_create_buildings = []


class Archery(Building):

    def get_allowed_tasks(self):
        return []

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 200}]
        self.allow_to_create_buildings = [HiddenPost()]


class Sawmill(Building):

    def get_allowed_tasks(self):
        return []

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 10
        self.building_resources_needed = [{Wood: 100}, {Metal: 100}, {Stone: 100}]
        self.allow_to_create_materials = {Plank: 1}
        self.allow_to_create_buildings = [Archery()]
