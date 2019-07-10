from src.models.Game import Game
from src.models.map.MapTile import MAX_INFLUENCE


def update_influences(game: Game):
    for user_id, user_game_model in game.user_game_models.items():
        user_game_model.war_influence_income = 0
        user_game_model.religion_influence_income = 0
        user_game_model.economic_influence_income = 0
        for building in user_game_model.buildings:
            user_game_model.war_influence_income += building.get_war_influence()
            user_game_model.economic_influence_income += building.get_economic_influence()
            user_game_model.religion_influence_income += building.religion_influence()


def process_turn(game: Game):
    game.map.clear_chaches()
    update_influences(game)
    for row in game.map.map:
        for tile in row:
            religion_influences = {}
            war_influences = {}
            econom_influences = {}

            if tile.userIdTown != -1:
                econom_influences[tile.userIdTown] += game.user_game_models[tile.userIdTown].economic_influence_income
                war_influences[tile.userIdTown] += game.user_game_models[tile.userIdTown].war_influence_income
                religion_influences[tile.userIdTown] += game.user_game_models[tile.userIdTown].religion_influence_income

            neghbours = game.map.get_neighbours(tile)
            for neghbour in neghbours:
                if neghbour.economicInfluence == MAX_INFLUENCE:
                    econom_influences[neghbour.economicDominationUserId] += game.user_game_models[neghbour.economicDominationUserId].economic_influence_income

                if neghbour.religionInfluence == MAX_INFLUENCE:
                    war_influences[neghbour.religionUserId] += game.user_game_models[neghbour.economicDominationUserId].war_influence_income

                if neghbour.warInfluence == MAX_INFLUENCE:
                    religion_influences[neghbour.warUserId] += game.user_game_models[neghbour.warUserId].religion_influence_income

            max_influence_income = -1
            second_after_max = -1
            user_id = -1
            for user_id, income_value in econom_influences.items():
                if income_value > max_influence_income:
                    user_id = user_id
                    second_after_max = max_influence_income
                    max_influence_income = income_value
            if tile.economicDominationUserId == user_id:
                tile.economicInfluence += max_influence_income - second_after_max
            else:
                tile.economicInfluence -= max_influence_income - second_after_max
            if tile.economicInfluence < 0:
                tile.economicDominationUserId = user_id
            if tile.economicInfluence > MAX_INFLUENCE:
                tile.economicInfluence = MAX_INFLUENCE

            max_influence_income = -1
            second_after_max = -1
            user_id = -1
            for user_id, income_value in war_influences.items():
                if income_value > max_influence_income:
                    user_id = user_id
                    second_after_max = max_influence_income
                    max_influence_income = income_value
            if tile.warUserId == user_id:
                tile.warInfluence += max_influence_income - second_after_max
            else:
                tile.warInfluence -= max_influence_income - second_after_max
            if tile.warInfluence < 0:
                tile.warUserId = user_id
            if tile.warInfluence > MAX_INFLUENCE:
                tile.warInfluence = MAX_INFLUENCE

            max_influence_income = -1
            second_after_max = -1
            user_id = -1
            for user_id, income_value in religion_influences.items():
                if income_value > max_influence_income:
                    user_id = user_id
                    second_after_max = max_influence_income
                    max_influence_income = income_value
            if tile.religionUserId == user_id:
                tile.religionInfluence += max_influence_income - second_after_max
            else:
                tile.religionInfluence -= max_influence_income - second_after_max
            if tile.religionInfluence < 0:
                tile.religionUserId = user_id
            if tile.religionInfluence > MAX_INFLUENCE:
                tile.religionInfluence = MAX_INFLUENCE
