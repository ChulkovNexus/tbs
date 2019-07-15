from src.models.map.Map import Map
from src.models.person.Person import Person
from src.models.tasks.Task import Task


class PrayerSongs(Task):

    def __init__(self, from_building, not_allowed_science_tasks, applied_buff):
        super().__init__()
        self.turns_count = 15
        self.from_building = from_building
        self.not_allowed_science_tasks = not_allowed_science_tasks
        self.applied_buff = applied_buff

    def __eq__(self, other):
        if isinstance(other, PrayerSongs):
            return other.from_building.__class__.name == self.from_building.__class__.name
        return False

    def check_conditions(self, map: Map, user_game_model, person: Person):
        return True

    def get_resources_for_consume(self):
        return {}

    def execute(self, user_game_model, person: Person):
        user_game_model.city_buffs.extends(self.applied_buff)

    def on_append_to_task_schedule(self):
        self.not_allowed_science_tasks.append(self)

    def on_remove_from_task_schedule(self):
        self.not_allowed_science_tasks.remove(self)
