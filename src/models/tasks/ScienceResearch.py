from src.models.map.Map import Map
from src.models.person.Person import Person
from src.models.tasks.Task import Task


class ScienceResearch(Task):

    def __init__(self, from_building, not_allowed_science_tasks):
        super().__init__()
        self.turns_count = 20
        # self.skill_for_calculating_turns = ScienceSkill
        self.from_building = from_building
        self.not_allowed_science_tasks = not_allowed_science_tasks

    def __eq__(self, other):
        if isinstance(other, ScienceResearch):
            return other.from_building.__class__.name == self.from_building.__class__.name
        return False

    def check_conditions(self, map: Map, user_game_model, person: Person):
        return True

    def get_resources_for_consume(self):
        return {}

    def execute(self, user_game_model, person: Person):
        user_game_model.science_points += 1

    def on_append_to_task_schedule(self):
        self.not_allowed_science_tasks.append(self)

    def on_remove_from_task_schedule(self):
        self.not_allowed_science_tasks.remove(self)
