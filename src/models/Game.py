import threading
from enum import Enum

from src.game_mutators import TaskManager, SpredInfluenceManager, MedicineProcessor
from src.game_mutators.bot import Bot
from src.models.map.Map import Map


class GameStatus(Enum):
    INITIAL = 1
    IN_PROGRESS = 2
    FINISHED = 3


class Game:

    def __init__(self):
        self.game_id = 0
        self.user_game_models = {}
        self.map = Map()
        self.thread: threading.Timer = None
        self.status = GameStatus.INITIAL

    def start_turn_timer(self):
        self.thread = threading.Timer(600.0, self.process_turn)
        self.thread.start()

    def process_turn(self):
        self.status = GameStatus.IN_PROGRESS
        self.start_turn_timer()
        TaskManager.execute_tasks(self)
        MedicineProcessor.process_turn(self.user_game_models)
        SpredInfluenceManager.process_turn(self)
        Bot.choose_tasks(self)

    def stop(self):
        self.status = GameStatus.FINISHED
        if self.thread:
            self.thread.cancel()
