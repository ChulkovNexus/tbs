import random


def choose_tasks(game):
    for user_id, user_game_model in game.user_game_models.items():
        user_game_model.logger.log_tasks(f"items stack - {user_game_model.items._items}")
        user_game_model.logger.log_tasks(f"buildings - {user_game_model.buildings}")
        for i, person in enumerate(user_game_model.persons):
            if not person.tasks_schedule and person.available_tasks:
                random_task = random.choice(person.available_tasks)
                person.tasks_schedule.append(random_task)
