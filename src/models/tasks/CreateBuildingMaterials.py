from src.models.map.Map import Map
from src.models.person.Person import Person
from src.models.tasks.Task import Task


class CreateBuildingMaterials(Task):

    def __init__(self, result, necessary_buildings):
        super().__init__()
        self.result = result
        self.necessary_buildings = necessary_buildings

    def execute(self, user_game_model, person):
        user_game_model.experience_increaser.increase_experience(1, person, person.craft_skill)
        for resource_type, count in self.result.items():
            extract_count = person.craft_skill.change_value_by_skill(count)
            user_game_model.resource_count_changer.extract_resources({resource_type: int(extract_count)})

    def check_conditions(self, map: Map, user_game_model, person: Person):
        has_buildings = all(x in user_game_model.buildings for x in self.necessary_buildings)
        return has_buildings

    def get_resources_for_consume(self):
        result = {}
        for resource_type, count in self.result.items():
            for needed_resource, needed_count in resource_type().needed_materials.items():
                result[needed_resource] = needed_count * count
        return result

    def __repr__(self):
        return f"CreateMaterials {self.result}"