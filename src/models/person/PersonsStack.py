
class PersonsStack(list):

    def __init__(self, user_game_model):
        super().__init__()
        self.user_game_model = user_game_model

    def append(self, other, n=1):
        list.append(self, other)
        other.on_append_to_user(self.user_game_model)
