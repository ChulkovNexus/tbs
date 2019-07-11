MAX_LEVEL = 10


class Skill:

    def __init__(self, level, difficulty=1):
        self.difficulty = difficulty
        self.level = level
        self.description = ""
        self.mutator = level
        self.experience = 0

    def change_value_by_skill(self, value):
        return value * (self.difficulty * self.get_multiplier_from_level())

    def get_multiplier_from_level(self):
        return {
            1: 0.6,
            2: 0.7,
            3: 0.8,
            4: 0.9,
            5: 1,
            6: 1.2,
            7: 1.4,
            8: 1.6,
            9: 1.8,
            10: 2
        }.get(self.get_level_with_mutator(), 0)

    def recalculate_experience(self):
        if self.experience in range(0, 5):
            self.level = 1
        elif self.experience in range(5, 10):
            self.level = 2
        elif self.experience in range(10, 20):
            self.level = 3
        elif self.experience in range(20, 40):
            self.level = 4
        elif self.experience in range(40, 80):
            self.level = 5
        elif self.experience in range(80, 160):
            self.level = 6
        elif self.experience in range(160, 240):
            self.level = 7
        elif self.experience in range(240, 480):
            self.level = 8
        elif self.experience in range(480, 960):
            self.level = 9
        elif self.experience > 960:
            self.level = 10

    def set_experience_from_level(self):
        self.experience = {
            1: 0,
            2: 5,
            3: 10,
            4: 20,
            5: 40,
            6: 80,
            7: 160,
            8: 240,
            9: 480,
            10: 960,
        }.get(self.level, 0)

    def get_level_with_mutator(self):
        level = self.level + self.mutator
        if level > MAX_LEVEL:
            level = MAX_LEVEL
        elif level < 0:
            level = 0
        return level
