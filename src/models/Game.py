from enum import Enum

from src.models.map.Map import Map


class GameStatus(Enum):
    INITIAL = 1
    IN_PROGRESS = 2


class Game:

    def __init__(self):
        self.game_id = 0
        self.user_game_models = {}
        self.map = Map()
        self.status = GameStatus.INITIAL
