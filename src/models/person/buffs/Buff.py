class Buff:

    def __init__(self):
        self.duration = 1


class CanStealMaterials(Buff):

    def __init__(self, level):
        super().__init__()
        self.duration = 99999
        self.level = level


class DefendFromStealMaterials(Buff):

    def __init__(self, level):
        super().__init__()
        self.duration = 99999
        self.level = level
