from src import GameServer
from src.game_mutators import TaskManager
from src.models.Game import Game
from src.models.Person import Person
from src.models.UserGameModel import UserGameModel
from src.models.UserModel import UserModel


def _create_persons_for_new_game(persons_stack):
    for i in range(0, 3):
        new_person = Person()
        persons_stack.append(new_person)


def _log_initial_params(game):
    for user_id, user_game_model in game.user_game_models.items():
        user_game_model.logger.enabled = True
        user_game_model.logger.log(f"user_id - {user_id} initial resources {user_game_model.extract_resource_availability_manager.available_resources}")

        if user_id != 0:
            user_game_model.logger.enabled = False


def itit_game(server: GameServer, users):
    server.games_counter += 1
    new_game = Game()
    new_game.game_id = server.games_counter

    def create_user_game_model(user: UserModel):
        user_game_model = UserGameModel()
        user_game_model.user_id = user.id
        user_game_model.game_id = server.games_counter
        _create_persons_for_new_game(user_game_model.persons)
        return user_game_model

    game_models_list = list(map(create_user_game_model, users))
    new_game.user_game_models = {i.user_id: i for i in game_models_list}
    new_game.map.fill_map(users)
    TaskManager.update_available_tasks_after_process_turn(new_game)
    server.games.append(new_game)
    _log_initial_params(new_game)
    return new_game


def _create_test_user(id):
    user = UserModel()
    user.id = id
    user.name = str(id)
    return user


def generate_test_users():
    return list(map(_create_test_user, range(8)))
