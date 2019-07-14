class AvailableTasksStack(list):

    def __init__(self, person):
        super().__init__()
        self.person = person
        self.logger = None
        self.listeners = list()

    def update_listeners(self):
        for listener in self.listeners:
            listener()

    def remove_listeners(self, listeners):
        for listener in listeners:
            if listener in self.listeners:
                self.listeners.remove(listener)
