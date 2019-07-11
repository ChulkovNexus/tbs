

class TaskSchedule(list):

    def __init__(self, person):
        super().__init__()
        self.person = person
        self.resource_count_changer = None

    def __add__(self, other):
        list.__add__(self, other)
        resources = other.get_resources_for_consume()
        self.resource_count_changer.consume_resources(resources, self.person)

    def __delitem__(self, **kwargs):
        item = list.__getitem__(self, **kwargs)
        resources = item.get_resources_for_consume()
        self.resource_count_changer.return_resources(resources, self.person)
        list.__delitem__(self, **kwargs)
