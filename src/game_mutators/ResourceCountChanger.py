from src.models.UserGameModel import UserGameModel
from src.game_mutators import TaskManager


class ResourceCountChanger:

    def __init__(self, user_game_model: UserGameModel):
        self.user_game_model = user_game_model

    def consume_resources(self, resources, person):
        for (resource_type, count) in resources:
            self.user_game_model.items.remove(resource_type, count)
        TaskManager.update_available_tasks_by_resources(self.user_game_model, person)

    def return_resources(self, resources, person):
        for (resource_type, count) in resources:
            self.user_game_model.items.add_item(resource_type, count)
        TaskManager.update_available_tasks_by_resources(self.user_game_model, person)

    def extract_resources(self, resources):
        for (resource_type, count) in resources:
            self.user_game_model.items.add_item(resource_type, count)
