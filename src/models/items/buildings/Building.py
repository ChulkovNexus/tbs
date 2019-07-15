from src.models.items.BuildingMaterials import Plank, Brick, Sail, MetalChunk
from src.models.items.Item import Item
from src.models.map.Resources import Wood, Metal, Stone, Lamb, Pigs, Hop
from src.models.person.buffs.Buff import CanStealMaterials, DefendFromStealMaterials
from src.models.tasks.PrayerSongs import PrayerSongs
from src.models.tasks.ScienceResearch import ScienceResearch


class Building(Item):


#возможно стоит переделать концепцию получение ресурсов их можно будет вырасщивать и продавать, но не факт
    def __init__(self):
        super().__init__()
        self.religion_influence = 0
        self.war_influence = 0
        self.economic_influence = 0
        self.building_turns_count = 1
        self.allow_to_create_materials = {}
        self.allow_to_create_buildings = []
        self.necessary_buildings = []
        self.apply_buffs = []
        self.building_resources_needed = [{}]

    def get_allowed_tasks(self, get_allowed_tasks):
        return []

    def __repr__(self):
        return f"{type(self).__name__}"


class Smelting(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Stone: 100}]
        self.allow_to_create_materials = {MetalChunk: 1}
        self.allow_to_create_buildings = [Blacksmith()]


class Blacksmith(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.building_resources_needed = [{Stone: 100, MetalChunk: 10}]
        self.allow_to_create_buildings = [MilitaryPost(), ResearchWorkshop()]


class MilitaryPost(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.apply_buffs = [DefendFromStealMaterials(1)]
        self.building_resources_needed = [{Stone: 200, MetalChunk: 10}]
        self.allow_to_create_buildings = [Fortress()]


class Fortress(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 8
        self.building_resources_needed = [{Stone: 200, Plank: 20, MetalChunk: 20}]
        self.allow_to_create_materials = {MetalChunk: 1}
        self.allow_to_create_buildings = [Stable()]


class Stable(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.building_resources_needed = [{Wood: 200, MetalChunk: 10}]
        self.allow_to_create_materials = {MetalChunk: 1}


class Totem(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.building_resources_needed = [{Wood: 200, MetalChunk: 10}]
        self.allow_to_create_materials = {MetalChunk: 1}

    def get_allowed_tasks(self, get_allowed_tasks):
        return [PrayerSongs(self, get_allowed_tasks)]


class Sanctuary(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.building_resources_needed = [{Wood: 200, MetalChunk: 10}]
        self.allow_to_create_materials = {MetalChunk: 1}

    def get_allowed_tasks(self, get_allowed_tasks):
        return [PrayerSongs(self, get_allowed_tasks)]


class Temple(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.war_influence = 4
        self.building_resources_needed = [{Wood: 200, MetalChunk: 10}]
        self.allow_to_create_materials = {MetalChunk: 1}

    def get_allowed_tasks(self, get_allowed_tasks):
        return [PrayerSongs(self, get_allowed_tasks)]


class HiddenPost(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 5
        self.war_influence = 2
        self.apply_buffs = [CanStealMaterials(1)]
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 200}]
        self.allow_to_create_buildings = []


class Archery(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 200}]
        self.allow_to_create_buildings = [HiddenPost()]


class Sawmill(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Wood: 100}, {Metal: 100}, {Stone: 100}]
        self.allow_to_create_materials = {Plank: 1}
        self.allow_to_create_buildings = [Archery()]


class BricksFactory(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Wood: 100}, {Metal: 100}, {Stone: 100}]
        self.allow_to_create_materials = {Brick: 1}
        self.allow_to_create_buildings = [Archery()]


class TradingPost(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 100, Brick: 10}]
        self.allow_to_create_buildings = [Market()]


class Market(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Plank: 5}, {Stone: 100, Brick: 10}]


class SandCareer(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 200, Stone: 200}]


class GlassWorkshop(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 15
        self.economic_influence = 10
        self.building_resources_needed = [{Plank: 30, Brick: 30}]


class LambFarm(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Lamb: 50}, {Stone: 100, Lamb: 50}]
        self.allow_to_create_buildings = [ClothFactory(), SausageShop()]


class PigsFarm(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Pigs: 50}, {Stone: 100, Pigs: 50}]
        self.allow_to_create_buildings = [ClothFactory(), SausageShop()]


class SausageShop(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 6
        self.building_resources_needed = [{Plank: 10, Lamb: 50}, {Brick: 10, Lamb: 50}, {Plank: 10, Pigs: 50}, {Brick: 10, Pigs: 50}]
        self.allow_to_create_buildings = [ClothFactory()]


class ClothFactory(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Plank: 15}, {Stone: 100, Brick: 10}]
        self.allow_to_create_buildings = [DressFactory(), SailFactory()]


class DressFactory(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Wood: 100, Plank: 15}, {Stone: 100, Brick: 10}]


class SailFactory(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.allow_to_create_materials = {Sail: 1}
        self.building_resources_needed = [{Wood: 100, Plank: 20}, {Stone: 100, Brick: 15}]


class Baloon(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Plank: 20, Sail: 20}]

    def get_allowed_tasks(self, get_allowed_tasks):
        return [ScienceResearch(self, get_allowed_tasks)]


class ResearchWorkshop(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.building_resources_needed = [{Plank: 20, Brick: 20}]

    def get_allowed_tasks(self, get_allowed_tasks):
        return [ScienceResearch(self, get_allowed_tasks)]


class Kitchen(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.allow_to_create_buildings = [DrugLab(), AlchemyLab(), HerbalMedicineHouse()]
        self.building_resources_needed = [{Wood: 100, Brick: 10}]


class HerbalMedicineHouse(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.allow_to_create_buildings = [Brewery()]
        self.building_resources_needed = [{Plank: 10}, {Wood: 10}] #todo icrese heal


class Brewery(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.economic_influence = 4
        self.building_resources_needed = [{Plank: 10, Hop: 100}, {Brick: 10, Hop: 100}]


class AlchemyLab(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.necessary_buildings = [Kitchen, ResearchWorkshop]
        self.allow_to_create_buildings = [DrugLab()]
        self.building_resources_needed = [{Plank: 20, Brick: 20}]

    def get_allowed_tasks(self, get_allowed_tasks):
        return [ScienceResearch(self, get_allowed_tasks)]


class DrugLab(Building):

    def __init__(self):
        super().__init__()
        self.building_turns_count = 10
        self.necessary_buildings = [Kitchen, AlchemyLab]
        self.building_resources_needed = [{Plank: 20, Brick: 20}]

    def get_allowed_tasks(self, get_allowed_tasks):
        return [ScienceResearch(self, get_allowed_tasks)]
