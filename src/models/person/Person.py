from src.models.person.AvailableTasksStack import AvailableTasksStack
from src.models.person.medicine.character_health import CharacterHealth
from src.models.tasks.TasksSchedule import TaskSchedule


class Person:

    def __init__(self, name):
        self.tasks_schedule = TaskSchedule(self)
        self.available_tasks = AvailableTasksStack(self)
        self.name = name
        self.gatherer_skill = None
        self.scientist_skill = None
        self.warrior_skill = None
        self.priest_skill = None
        self.craft_skill = None
        self.buffs = list()
        self.health = CharacterHealth(self)

    def on_append_to_user(self, user_game_model):
        self.tasks_schedule.resource_count_changer = user_game_model.resource_count_changer
        self.tasks_schedule.logger = user_game_model.logger

    def recalculate_experience(self):
        self.gatherer_skill.recalculate_experience()
        self.scientist_skill.recalculate_experience()
        self.warrior_skill.recalculate_experience()
        self.priest_skill.recalculate_experience()
        self.craft_skill.recalculate_experience()

    def log_skill_levels(self, logger):
        logger.log_tasks(f"person - {self.name}")
        logger.log_tasks(f"   gatherer_skill - {self.gatherer_skill.level} expirience- {self.gatherer_skill.experience}")
        logger.log_tasks(f"   scientist_skill - {self.scientist_skill.level} expirience- {self.scientist_skill.experience}")
        logger.log_tasks(f"   warrior_skill - {self.warrior_skill.level} expirience- {self.warrior_skill.experience}")
        logger.log_tasks(f"   priest_skill - {self.priest_skill.level} expirience- {self.priest_skill.experience}")
        logger.log_tasks(f"   craft_skill - {self.craft_skill.level} expirience- {self.craft_skill.experience}")
