class UserModelLogger:

    def __init__(self):
        self.tasks_log_enabled = False
        self.influence_log = False

    def log_tasks(self, string):
        if self.tasks_log_enabled:
            print(string)

    def log_influence(self, string):
        if self.influence_log:
            print(string)