from src.models.Game import Game
from src.models.Person import Person
from src.models.UserGameModel import UserGameModel


def execute_tasks(game: Game):
    for user_id, user_game_model in game.user_game_models.items():
        for person in user_game_model.persons:
            last_task = person.tasks_schedule.pop(0)
            if last_task.check_conditions(game.map, user_game_model, person):
                last_task.execute()


def update_available_tasks_after_process_turn(game: Game):
    for user_id, user_game_model in game.user_game_models.items():
        for person in user_game_model.persons:
            user_resources = game.map.get_user_resources()
            user_game_model.extract_resource_task_availability_manager.available_resources = user_resources
            _update_available_tasks(user_game_model, person)


def _update_available_tasks(game_model: UserGameModel, person: Person):
    game_model.extract_resource_task_availability_manager.clear_cache()
    game_model.resorce_dependend_tasks_manager.clear_cache()
    game_model.buildings_dependend_tasks_manager.clear_cache()

    resources_in_stock = game_model.items.get_resources()
    person.available_tasks.extend(game_model.extract_resource_task_availability_manager.get_tasks())
    buildings_tasks = game_model.buildings_dependend_tasks_manager.get_tasks(game_model.buildings)
    person.available_tasks.extend(game_model.resorce_dependend_tasks_manager.get_tasks(buildings_tasks, resources_in_stock))


def update_available_tasks_by_resources(game_model: UserGameModel, person: Person):
    game_model.resorce_dependend_tasks_manager.clear_cache()
    resources_in_stock = game_model.items.get_resources()

    buildings_tasks = game_model.buildings_dependend_tasks_manager.get_tasks(game_model.buildings)
    person.available_tasks.extend(game_model.resorce_dependend_tasks_manager.get_tasks(buildings_tasks, resources_in_stock))
