from src.game_mutators.ExperienceIncreaser import ExperienceIncreaser
from src.game_mutators.ResourceCountChanger import ResourceCountChanger
from src.models.Influence import Influence
from src.models.person.PersonsStack import PersonsStack
from src.models.items.ItemsStack import ItemsStack
from src.models.tasks.availability_callbacks.BuildingsDependendTasksManager import BuildingsDependedTasksManager
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
        self.war_influence = Influence()
        self.economic_influence = Influence()
        self.religion_influence = Influence()
        self.buildings_dependend_tasks_manager = BuildingsDependedTasksManager()
        self.extract_resource_availability_manager = ExtractResourceTaskAvailabilityManager()
        self.resorce_dependend_tasks_manager = ResorceDependendTasksManager()

