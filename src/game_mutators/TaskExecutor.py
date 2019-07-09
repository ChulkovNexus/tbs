from src.models.Game import Game


def execute_tasks(game: Game):
    for game_model in game.user_game_models:
        for person in game_model.persons:
            last_task = person.tasks_schedule.pop(0)
            if last_task.check_conditions(,:
                last_task.execute()
