class UserModelLogger:

    def __init__(self):
        self.tasks_log_enabled = False

    def log_tasks(self, string):
        if self.tasks_log_enabled:
            print(string)
