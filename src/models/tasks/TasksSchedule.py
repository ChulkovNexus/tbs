

class TaskSchedule(list):

    def __init__(self):
        super().__init__()

    def __delitem__(self, **kwargs):
        item = list.__getitem__(self, **kwargs)
        item.return_resources()
        list.__delitem__(self, **kwargs)
