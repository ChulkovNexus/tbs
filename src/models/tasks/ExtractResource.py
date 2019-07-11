from src.models.Person import Person
from src.models.map import Map
from src.models.map.Resources import Resource
from src.models.tasks.Task import Task


class ExtractResource(Task):

    def __init__(self, resource: Resource):
        super().__init__()
        self.resource = resource

    def execute(self, user_game_model, person: Person):
        user_game_model.resource_count_changer.extract_resources({self.resource: 10})

    def check_conditions(self, map: Map, user_game_model, person: Person):
        tiles = map.get_tiles_with_economic_influence(user_game_model.user_id)
        for tile in tiles:
            for resource in tile.resources:
                if type(resource) == type(self.resource):
                    return True
        return False

    def __repr__(self):
        return f"ExtractResource {self.resource}"
