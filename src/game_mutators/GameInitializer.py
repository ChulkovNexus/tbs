import random

from src import GameServer
from src.game_mutators import TaskManager
from src.models.Game import Game
from src.models.person.Person import Person
from src.models.UserGameModel import UserGameModel
from src.models.UserModel import UserModel
from src.models.person.Skill import Skill


class SkillPointsHolder:
    def __init__(self):
        self.poins = 20

    def get_rand_int(self):
        randint = random.randint(0, 5)
        skill_poins = self.poins - randint
        return 0 if skill_poins < 0 else randint


def _create_persons_for_new_game(persons_stack):
    for i in range(0, 1):
        new_person = Person(i)
        _fill_skills(new_person)
        persons_stack.append(new_person)


def _log_initial_params(game):
    for user_id, user_game_model in game.user_game_models.items():
        user_game_model.logger.log_tasks(f"user_id - {user_id} initial resources {user_game_model.extract_resource_availability_manager.available_resources}")


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


def _fill_skills(person):
    skill_points = SkillPointsHolder()
    person.gatherer_skill = Skill(skill_points.get_rand_int())
    person.scientist_skill = Skill(skill_points.get_rand_int())
    person.warrior_skill = Skill(skill_points.get_rand_int())
    person.priest_skill = Skill(skill_points.get_rand_int())
    person.economist_skill = Skill(skill_points.get_rand_int())
    person.craft_skill = Skill(skill_points.get_rand_int())
    if skill_points.poins > 0:
        person.gatherer_skill.level += 1
        person.scientist_skill.level += 1
        person.warrior_skill.level += 1
        person.priest_skill.level += 1
        person.economist_skill.level += 1
        person.craft_skill.level += 1
    person.gatherer_skill.set_experience_from_level()
    person.scientist_skill.set_experience_from_level()
    person.warrior_skill.set_experience_from_level()
    person.priest_skill.set_experience_from_level()
    person.economist_skill.set_experience_from_level()
    person.craft_skill.set_experience_from_level()


def generate_test_users():
    return list(map(_create_test_user, range(8)))
