

class TaskSchedule(list):

    def __init__(self, person):
        super().__init__()
        self.person = person
        self.resource_count_changer = None
        self.logger = None

    def append(self, other, n=1):
        list.append(self, other)
        other.on_append_to_task_schedule()
        resources = other.get_resources_for_consume()
        self.resource_count_changer.consume_resources(resources, self.person)

    def __delitem__(self, **kwargs):
        item = list.__getitem__(self, **kwargs)
        resources = item.get_resources_for_consume()
        item.on_remove_from_task_schedule()
        self.resource_count_changer.return_resources(resources, self.person)
        list.__delitem__(self, **kwargs)
