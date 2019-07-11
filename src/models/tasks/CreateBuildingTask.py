from src.models.map.Map import Map
from src.models.person.Person import Person
from src.models.tasks.Task import Task


class CreateBuilding(Task):

    def __init__(self, result_building):
        super().__init__()
        self.result_building = result_building
        self.turns_count = result_building.building_turns_count

    def check_conditions(self, map: Map, user_game_model, person: Person):
        resources = user_game_model.items.get_resources()
        necessary_resources = self.get_resources_for_consume()
        return all([key in resources and resources[key] > necessary_resources[key] for key in necessary_resources.keys()])

    def get_resources_for_consume(self):
        return self.result_building.building_resources_needed

    def execute(self, user_game_model, person: Person):
        user_game_model.experience_increaser.increase_experience(self.result_building.building_turns_count, person, person.craft_skill)
        user_game_model.append(self.result_building)
