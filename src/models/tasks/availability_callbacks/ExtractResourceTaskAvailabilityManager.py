from src.models.tasks.ExtractResource import ExtractResource


class ExtractResourceTaskAvailabilityManager:

    def __init__(self):
        self._task_list = list()
        self.available_resources = list()

    def get_tasks(self):
        if not self._task_list:
            for resource in self.available_resources:
                self._task_list.append(ExtractResource(resource))
        return self._task_list

    def clear_cache(self):
        self._task_list.clear()
