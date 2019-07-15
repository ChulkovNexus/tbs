from src.models.map.Map import Map
from src.models.person.Person import Person
from src.models.tasks.Task import Task


class CreateBuilding(Task):

    def __init__(self, result_building, needed_materials, not_allowed_buildings):
        super().__init__()
        self.result_building = result_building
        self.needed_materials = needed_materials
        self.not_allowed_buildings = not_allowed_buildings
        self.turns_count = result_building.building_turns_count

    def check_conditions(self, map: Map, user_game_model, person: Person):
        return self.result_building not in user_game_model.buildings

    def get_resources_for_consume(self):
        return self.needed_materials

    def execute(self, user_game_model, person: Person):
        user_game_model.experience_increaser.increase_experience(self.result_building.building_turns_count, person, person.craft_skill)
        user_game_model.buildings.append(self.result_building)
        user_game_model.city_buffs.extends(self.result_building.apply_buffs)

    def on_append_to_task_schedule(self):
        self.not_allowed_buildings.append(self.result_building)

    def on_remove_from_task_schedule(self):
        self.not_allowed_buildings.remove(self.result_building)

    def __repr__(self):
        return f"CreateBuilding {self.result_building}"
