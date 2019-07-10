from src.models.Person import Person
from src.models.UserGameModel import UserGameModel
from src.models.map import Map
from src.models.map.Resources import Resource
from src.models.tasks.Task import Task


class ExtractResource(Task):

    def __init__(self, resource: Resource):
        super().__init__()
        self.resource = resource

    def execute(self, user_game_model: UserGameModel, person: Person):
        user_game_model.items.add_item(self.resource)

    def check_conditions(self, map: Map, user_game_model: UserGameModel, person: Person):
        tiles = map.get_tiles_with_economic_influence(user_game_model.user_id)
        for tile in tiles:
            for resource in tile.resources:
                if type(resource) == type(Resource):
                    return True
        return False