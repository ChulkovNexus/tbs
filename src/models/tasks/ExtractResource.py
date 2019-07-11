from src.models.person.Person import Person
from src.models.map import Map
from src.models.map.Resources import Resource
from src.models.tasks.Task import Task

DEFAULT_EXTRACT_VALUE = 10


class ExtractResource(Task):

    def __init__(self, resource: Resource):
        super().__init__()
        self.resource = resource

    def execute(self, user_game_model, person: Person):
        extract_count = person.gatherer_skill.change_value_by_skill(DEFAULT_EXTRACT_VALUE)
        user_game_model.experience_increaser.increase_experience(self.resource.resource_tier, person, person.gatherer_skill)
        user_game_model.resource_count_changer.extract_resources({self.resource: int(extract_count)})

    def check_conditions(self, map: Map, user_game_model, person: Person):
        tiles = map.get_tiles_with_economic_influence(user_game_model.user_id)
        for tile in tiles:
            for resource in tile.resources:
                if type(resource) == type(self.resource):
                    return True
        return False

    def __repr__(self):
        return f"ExtractResource {self.resource}"

    def get_resources_for_consume(self):
        pass
