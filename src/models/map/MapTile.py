MAX_INFLUENCE = 100


class MapTile:

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.resources = list()
        self.userIdTown = -1
        self.economicDominationUserId = -1
        self.economicInfluence = 0
        self.religionUserId = -1
        self.religionInfluence = 0
        self.warUserId = -1
        self.warInfluence = 0
