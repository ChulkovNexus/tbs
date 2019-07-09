from enum import Enum


class ItemType(Enum):
    Default = 0
    Resource = 0


class Item:

    def __init__(self):
        self.type = ItemType.Default


