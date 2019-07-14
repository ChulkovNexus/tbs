class TaskSchedule(list):

    def __init__(self, person):
        super().__init__()
        self.person = person
        self.resource_count_changer = None
        self.logger = None
        self.listeners = list()

    def append(self, other, n=1):
        list.append(self, other)
        other.on_append_to_task_schedule()
        self.update_listeners()
        resources = other.get_resources_for_consume()
        self.resource_count_changer.consume_resources(resources, self.person)

    def remove(self, **kwargs):
        print(f"removed from tasks schedule")
        item = list.__getitem__(self, **kwargs)
        resources = item.get_resources_for_consume()
        item.on_remove_from_task_schedule()
        self.update_listeners()
        self.resource_count_changer.return_resources(resources, self.person)
        list.__delitem__(self, **kwargs)

    def update_listeners(self):
        for listener in self.listeners:
            listener()

    def remove_listeners(self, listeners):
        for listener in listeners:
            if listener in self.listeners:
                self.listeners.remove(listener)
