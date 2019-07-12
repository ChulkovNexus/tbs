from src.game_mutators import TaskManager


class ResourceCountChanger:

    def __init__(self, user_game_model):
        self.user_game_model = user_game_model

    def consume_resources(self, resources, person):
        for resource_type, count in resources.items():
            self.user_game_model.items.remove(resource_type, count)
        self.update_persons_tasks()

    def return_resources(self, resources, person):
        for resource_type, count in resources.items():
            self.user_game_model.items.add_item(resource_type, count)
        self.update_persons_tasks()

    def extract_resources(self, resources):
        for resource_type, count in resources.items():
            self.user_game_model.items.add_item(resource_type, count)

    def update_persons_tasks(self):
        for person in self.user_game_model.persons:
            TaskManager.update_available_tasks_by_resources(self.user_game_model, person)
