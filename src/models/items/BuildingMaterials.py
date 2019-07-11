from src.models.items.Item import Item
from src.models.map.Resources import Wood, Stone


class BuildingMaterials(Item):

    def __init__(self):
        super().__init__()
        self.needed_materials = {}


class Plank(BuildingMaterials):

    def __init__(self):
        super().__init__()
        self.needed_materials = {Wood: 10}


class Brick(BuildingMaterials):

    def __init__(self):
        super().__init__()
        self.needed_materials = {Stone: 10}
