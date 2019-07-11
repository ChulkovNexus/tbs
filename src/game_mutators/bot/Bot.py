import random


def choose_tasks(game):
    for user_id, user_game_model in game.user_game_models.items():
        user_game_model.logger.log(f"items stack - {user_game_model.items._items}")
        for i, person in enumerate(user_game_model.persons):
            random_task = random.choice(person.available_tasks)
            person.tasks_schedule.append(random_task)
            user_game_model.logger.log(f"person - {i} available tasks - {person.available_tasks} task chosen - {random_task}")