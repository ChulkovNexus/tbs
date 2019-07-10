import random

from src.models.map.Direction import Direction
from src.models.map.MapTile import MapTile, MAX_INFLUENCE
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


all_directions = [Direction(-1, -1), Direction(0, -1), Direction(1, -1), Direction(-1, 0), Direction(1, 0),
                  Direction(-1, 1), Direction(0, 1), Direction(1, 1)]


def get_noth_west_neighbour(pattern, x, y):
    if x > 0 and y > 0:
        return pattern[y - 1][x - 1], all_directions[0]


def get_noth_neighbour(pattern, x, y):
    if y > 0:
        return pattern[y - 1][x], all_directions[1]


def get_noth_east_neighbour(pattern, x, y):
    if y > 0 and x < pattern[y].__len__() - 1:
        return pattern[y - 1][x + 1], all_directions[2]


def get_west_neighbour(pattern, x, y):
    if x > 0:
        return pattern[y][x - 1], all_directions[3]


def get_east_neighbour(pattern, x, y):
    if x < pattern[y].__len__() - 1:
        return pattern[y][x + 1], all_directions[4]


def get_south_west_neighbour(pattern, x, y):
    if x > 0 and y < pattern.__len__() - 1:
        return pattern[y + 1][x - 1], all_directions[5]


def get_south_neighbour(pattern, x, y):
    if y < pattern.__len__() - 1:
        return pattern[y + 1][x], all_directions[6]


def get_south_east_neighbour(pattern, x, y):
    if y < pattern.__len__() - 1 and x < pattern[y].__len__() - 1:
        return pattern[y + 1][x + 1], all_directions[7]


def get_neighbours(pattern, x, y):
    if y > pattern.__len__() or x > pattern[0].__len__():
        raise ValueError('get_neighbours wrong request')
    return [get_noth_west_neighbour(pattern, x, y), get_noth_neighbour(pattern, x, y),
            get_noth_east_neighbour(pattern, x, y), get_west_neighbour(pattern, x, y),
            get_east_neighbour(pattern, x, y), get_south_west_neighbour(pattern, x, y),
            get_south_neighbour(pattern, x, y), get_south_east_neighbour(pattern, x, y)]


class Map:

    def __init__(self):
        self.map = [[MapTile(x, y) for y in range(5)] for x in range(5)]

        # we have to clear it every turn
        self.religion_influence_cache = {}
        self.economic_influence_cache = {}
        self.war_influence_cache = {}
        self.resources_cache = {}

    def clear_chaches(self):
        self.religion_influence_cache.clear()
        self.economic_influence_cache.clear()
        self.war_influence_cache.clear()
        self.resources_cache.clear()

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
                        tile.religionUserId = users[counter].user_id
                        tile.economicDominationUserId = users[counter].user_id
                        tile.warUserId = users[counter].user_id
                        tile.warInfluence = MAX_INFLUENCE
                        tile.economicInfluence = MAX_INFLUENCE
                        tile.religionInfluence = MAX_INFLUENCE
                        counter += 1

        self.fill_map_with_resources()

    def get_tiles_with_economic_influence(self, user_id):
        if self.economic_influence_cache[user_id]:
            return self.economic_influence_cache[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.economicDominationUserId == user_id:
                    result.append(tile)

        self.economic_influence_cache[user_id] = result
        return result

    def get_tiles_with_religion_influence(self, user_id):
        if self.religion_influence_cache[user_id]:
            return self.religion_influence_cache[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.religionUserId == user_id:
                    result.append(tile)
        self.religion_influence_cache[user_id] = result
        return result

    def get_tiles_with_war_influence(self, user_id):
        if self.war_influence_cache[user_id]:
            return self.war_influence_cache[user_id]
        result = list()
        for row in self.map:
            for tile in row:
                if tile.warUserId == user_id:
                    result.append(tile)
        self.war_influence_cache[user_id] = result
        return result

    def get_user_resources(self, user_id):
        if self.resources_cache[user_id]:
            return self.resources_cache[user_id]
        result = list()
        tiles = self.get_tiles_with_economic_influence(user_id)
        for tile in tiles:
            not_in_result_resources = [res for res in tile.resources if res not in result]
            result.extend(not_in_result_resources)

        self.resources_cache[user_id] = result
        return result

    def get_neighbours(self, tile):
        neighbours = get_neighbours(self.map, tile.pos_x, tile.pos_y)
        return [neighbour[0] for neighbour in neighbours if neighbour is not None]
