from src.game_mutators.ExperienceIncreaser import ExperienceIncreaser
from src.game_mutators.ResourceCountChanger import ResourceCountChanger
from src.models.PersonsStack import PersonsStack
from src.models.items.ItemsStack import ItemsStack
from src.models.tasks.availability_callbacks.BuildingsDependendTasksManager import BuildingsDependendTasksManager
from src.models.tasks.availability_callbacks.ExtractResourceTaskAvailabilityManager import ExtractResourceTaskAvailabilityManager
from src.models.tasks.availability_callbacks.ResorceDependendTasksManager import ResorceDependendTasksManager
from src.utils.UserModelLogger import UserModelLogger


class UserGameModel:

    def __init__(self):
        self.user_id = 0
        self.game_id = 0
        self.pos_x = 0
        self.pos_y = 0
        self.logger = UserModelLogger()
        self.resource_count_changer = ResourceCountChanger(self)
        self.experience_increaser = ExperienceIncreaser(self)
        self.persons = PersonsStack(self)
        self.items = ItemsStack()
        self.buildings = list()
        self.war_influence_income = 0
        self.economic_influence_income = 0
        self.religion_influence_income = 0
        self.buildings_dependend_tasks_manager = BuildingsDependendTasksManager()
        self.extract_resource_availability_manager = ExtractResourceTaskAvailabilityManager()
        self.resorce_dependend_tasks_manager = ResorceDependendTasksManager()

