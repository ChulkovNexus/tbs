class ResorceDependendTasksManager:

    def __init__(self , logger):
        self._task_list = list()
        self.logger = logger

    def get_tasks(self, tasks, resources):
        if not self._task_list:
            for task in tasks:
                task_resources = task.get_resources_for_consume()
                if all([key in resources and resources[key] > task_resources[key] for key in task_resources.keys()]):
                    self._task_list.append(task)

        return self._task_list

    def clear_cache(self):
        self._task_list.clear()
