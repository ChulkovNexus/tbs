

if __name__ == "__main__":
    from src.GameServer import GameServer
    from src.game_mutators import GameInitializer
    from src.models.UserModel import UserModel

    game_server = GameServer()
    users = GameInitializer.generate_test_users()
    game = GameInitializer.itit_game(game_server, users)
    game.process_turn()
