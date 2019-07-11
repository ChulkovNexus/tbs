from src.models.tasks.TasksSchedule import TaskSchedule


class Person:

    def __init__(self):
        self.tasks_schedule = TaskSchedule(self)
        self.available_tasks = list()

    def on_append_to_user(self, user_game_model):
        self.tasks_schedule.resource_count_changer = user_game_model.resource_count_changer
