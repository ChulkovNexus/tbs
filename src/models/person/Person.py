from src.models.person.medicine.character_health import CharacterHealth
from src.models.tasks.TasksSchedule import TaskSchedule


class Person:

    def __init__(self, name):
        self.tasks_schedule = TaskSchedule(self)
        self.available_tasks = list()
        self.name = name
        self.gatherer_skill = None
        self.scientist_skill = None
        self.warrior_skill = None
        self.priest_skill = None
        self.economist_skill = None
        self.craft_skill = None
        self.buffs = list()
        self.health = CharacterHealth(self)

    def on_append_to_user(self, user_game_model):
        self.tasks_schedule.resource_count_changer = user_game_model.resource_count_changer

    def recalculate_experience(self):
        self.gatherer_skill.recalculate_experience()
        self.scientist_skill.recalculate_experience()
        self.warrior_skill.recalculate_experience()
        self.priest_skill.recalculate_experience()
        self.economist_skill.recalculate_experience()
        self.craft_skill.recalculate_experience()

    def log_skill_levels(self, logger):
        logger.log(f"person - {self.name}")
        logger.log(f"   gatherer_skill - {self.gatherer_skill.level}")
        logger.log(f"   scientist_skill - {self.scientist_skill.level}")
        logger.log(f"   warrior_skill - {self.warrior_skill.level}")
        logger.log(f"   priest_skill - {self.priest_skill.level}")
        logger.log(f"   economist_skill - {self.economist_skill.level}")
        logger.log(f"   craft_skill - {self.craft_skill.level}")
