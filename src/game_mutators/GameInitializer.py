from src import GameServer
from src.models.Game import Game
from src.models.Person import Person
from src.models.UserGameModel import UserGameModel
from src.models.UserModel import UserModel


def _create_persons_for_new_game():
    persons_list = list()
    for i in range(0, 3):
        new_person = Person()
        persons_list.append(new_person)
    return persons_list


def itit_game(server: GameServer, users):
    server.games_counter += 1
    new_game = Game()
    new_game.game_id = server.games_counter

    def create_user_game_model(user: UserModel):
        user_game_model = UserGameModel()
        user_game_model.user_id = user.id
        user_game_model.game_id = server.games_counter
        user_game_model.persons = _create_persons_for_new_game()
        return user_game_model

    new_game.user_game_models = list(map(create_user_game_model, users))
    new_game.map.fill_map(users)
    server.games.append(new_game)


def _create_test_user(id):
    user = UserModel()
    user.id = id
    user.name = str(id)
    return user


def generate_test_users():
    return list(map(_create_test_user, range(8)))