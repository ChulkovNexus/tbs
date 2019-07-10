from src.models.tasks.TasksSchedule import TaskSchedule


class Person:

    def __init__(self):
        self.tasks_schedule = TaskSchedule()
        self.available_tasks = list()
