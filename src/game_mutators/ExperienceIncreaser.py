
class ExperienceIncreaser:

    def __init__(self, user_game_model):
        self.user_game_model = user_game_model

    def increase_experience(self, value, person, skill):
        skill.experience += value