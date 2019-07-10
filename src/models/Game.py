import threading
from enum import Enum

from src.game_mutators import TaskManager, SpredInfluenceManager
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

    def start_turn_timer(self):
        self.thread = threading.Timer(5.0, self.process_turn)
        self.thread.start()

    def process_turn(self):
        self.start_turn_timer()
        TaskManager.execute_tasks(self)
        SpredInfluenceManager.process_turn(self)
