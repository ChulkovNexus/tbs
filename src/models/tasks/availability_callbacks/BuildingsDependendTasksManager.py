class BuildingsDependendTasksManager:
    task_not_needed_buildings = {}

    def __init__(self):
        self._task_list = list()

    def get_tasks(self, buildings):
        if not self._task_list:
            for building in buildings:
                tasks = building.get_allowed_tasks()
                self._task_list.extend([x for x in tasks if x not in self._task_list])
        return self._task_list

    def clear_cache(self):
        self._task_list.clear()
