import random
from src.models.map.MapTile import MapTile
from src.models.map.Resources import first_tier_food_resource, first_tier_material_resource, second_tier_material_resource, second_tier_food_resource, third_tier_material_resource


def fill_with_third_level_resources(tile):
    tile.resources.append(random.choice(first_tier_food_resource))
    tile.resources.append(random.choice(first_tier_material_resource))
    tile.resources.append(random.choice(second_tier_material_resource))
    tile.resources.append(random.choice(second_tier_food_resource))
    tile.resources.append(random.choice(third_tier_material_resource))


def fill_with_first_level_resources(tile):
    tile.resources.append(random.choice(first_tier_food_resource))
    tile.resources.append(random.choice(first_tier_material_resource))


def fill_with_second_level_resources(tile):
    tile.resources.append(random.choice(first_tier_food_resource))
    tile.resources.append(random.choice(first_tier_material_resource))
    tile.resources.append(random.choice(second_tier_material_resource))
    tile.resources.append(random.choice(second_tier_food_resource))


class Map:

    def __init__(self):
        self.map = [[MapTile(x, y) for y in range(5)] for x in range(5)]
        
        # we have to clear it every turn
        self.religion_influence_cash = {}
        self.economic_influence_cash = {}
        self.war_influence_cash = {}
        self.resources_cash = {}

    def fill_map_with_resources(self):
        for row in self.map:
            for tile in row:
                if tile.pos_x == 2 and tile.pos_y == 2:
                    fill_with_third_level_resources(tile)
                elif tile.userIdTown != -1:
                    fill_with_first_level_resources(tile)
                else:
                    fill_with_second_level_resources(tile)

    def fill_map(self, users):
        counter = 0
        for x, row in enumerate(self.map):
            if x % 2 == 0:
                for y, tile in enumerate(row):
                    if x % 2 == 0 and x != 2 and y != 2:
                        tile.userIdTown = users[counter].user_id
                        counter += 1

        self.fill_map_with_resources()

    def get_tiles_with_economic_influence(self, user_id):
        if self.economic_influence_cash[user_id]:
            return self.economic_influence_cash[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.economicDominationUserId == user_id:
                    result.append(tile)

        self.economic_influence_cash[user_id] = result
        return result

    def get_tiles_with_religion_influence(self, user_id):
        if self.religion_influence_cash[user_id]:
            return self.religion_influence_cash[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.religionUserId == user_id:
                    result.append(tile)
        self.religion_influence_cash[user_id] = result
        return result

    def get_tiles_with_war_influence(self, user_id):
        if self.war_influence_cash[user_id]:
            return self.war_influence_cash[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.warUserId == user_id:
                    result.append(tile)
        self.war_influence_cash[user_id] = result
        return result

    def get_user_resources(self, user_id):
        if self.resources_cash[user_id]:
            return self.resources_cash[user_id]
        result = list()
        tiles = self.get_tiles_with_economic_influence(user_id)
        for tile in tiles:
            not_in_result_resources = [res for res in tile.resources if res not in result]
            result.extend(not_in_result_resources)

        self.resources_cash[user_id] = result
        return result
