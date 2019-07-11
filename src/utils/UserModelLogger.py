class UserModelLogger:

    def __init__(self):
        self.enabled = False

    def log(self, string):
        if self.enabled:
            print(string)
