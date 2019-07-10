from src.GameServer import GameServer
from src.game_mutators import GameInitializer
from src.models.UserModel import UserModel

if __name__ == "__main__":
    game_server = GameServer()
    users = GameInitializer.generate_test_users()
    game = GameInitializer.itit_game(game_server, users)
    game.start_game()
