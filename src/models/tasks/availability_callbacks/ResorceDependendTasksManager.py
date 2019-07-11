class ResorceDependendTasksManager:

    def __init__(self):
        self._task_list = list()

    def get_tasks(self, tasks, resources):
        if not self._task_list:
            for task in tasks:
                task_reses = task.get_resources_for_consume()
                if all(x in resources for x in task_reses):
                    self._task_list.append(task)

        return self._task_list

    def clear_cache(self):
        self._task_list.clear()
