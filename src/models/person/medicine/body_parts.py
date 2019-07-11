from abc import abstractmethod
from enum import Enum

import random


class PartFunctionality:

    def __init__(self, sight, hands_effectivity, movement_effectivity, nutrition_effectivity, ill_resistance_effectivity):
        self.sight = sight
        self.hands_effectivity = hands_effectivity
        self.movement_effectivity = movement_effectivity
        self.nutrition_effectivity = nutrition_effectivity
        self.ill_resistance_effectivity = ill_resistance_effectivity


class BodyPartInterface:

    @abstractmethod
    def get_part_functionality(self): raise NotImplementedError

    @abstractmethod
    def get_sub_part(self): raise NotImplementedError


class ChestSubParts(BodyPartInterface, Enum):
    Hart = 1, PartFunctionality(0, 30, 30, 0, 30)
    Liver = 2, PartFunctionality(0, 0, 0, 30, 30)
    Stomach = 3, PartFunctionality(0, 0, 0, 100, 30)
    Spine = 4, PartFunctionality(0, 30, 100, 100, 30)

    def get_part_functionality(self):
        return self.value[1]

    def get_sub_part(self):
        return None


class LimbSubParts(BodyPartInterface, Enum):
    Forefinger = 1, PartFunctionality(0, 10, 10, 0, 0)
    Middle_finger = 2, PartFunctionality(0, 10, 10, 0, 0)
    Thumb = 3, PartFunctionality(0, 10, 10, 0, 0)
    Pinky = 4, PartFunctionality(0, 10, 10, 0, 0)

    def get_part_functionality(self):
        return self.value[1]

    def get_sub_part(self):
        return None


class HeadSubParts(BodyPartInterface, Enum):
    LeftEye = 1, PartFunctionality(50, 0, 0, 0, 0)
    RightEye = 2, PartFunctionality(0, 0, 0, 0, 0)
    LeftEar = 3, PartFunctionality(0, 0, 0, 0, 0)
    RightEar = 4, PartFunctionality(0, 0, 0, 0, 0)
    Nose = 5, PartFunctionality(0, 0, 0, 0, 10)

    def get_part_functionality(self):
        return self.value[1]

    def get_sub_part(self):
        return None


class BodyParts(Enum):
    Head = 1, HeadSubParts, PartFunctionality(50, 0, 0, 30, 0)
    RightHand = 2, LimbSubParts, PartFunctionality(0, 50, 0, 0, 0)
    LeftHand = 3, LimbSubParts, PartFunctionality(0, 50, 0, 0, 0)
    RightFoot = 4, LimbSubParts, PartFunctionality(0, 0, 50, 0, 0)
    LeftFoot = 5, LimbSubParts, PartFunctionality(0, 0, 50, 0, 0)
    Chest = 6, ChestSubParts, PartFunctionality(0, 30, 30, 0, 0)

    def get_part_functionality(self):
        return self.value[2]

    def get_sub_part(self):
        return self.value[1]


_body_parts = list(BodyParts)


def get_random_body_part():
    return random.choice(_body_parts)


class BodyPart:

    def __init__(self, part):
        self.destruction_level = 0
        self.part = part
        self.sub_parts = self._generate_sub_parts()

    def get_functionality_affect(self):
        functionality = self.part.get_part_functionality()
        sight = functionality.sight * self.destruction_level / 100
        hands_effectivity = functionality.hands_effectivity * self.destruction_level / 100
        movement_effectivity = functionality.movement_effectivity * self.destruction_level / 100
        nutrition_effectivity = functionality.nutrition_effectivity * self.destruction_level / 100
        ill_resistance_effectivity = functionality.ill_resistance_effectivity * self.destruction_level / 100

        if self.sub_parts:
            for sub_part in self.sub_parts:
                functionality = sub_part.part.get_part_functionality()
                sight += functionality.sight * sub_part.destruction_level / 100
                hands_effectivity += functionality.hands_effectivity * sub_part.destruction_level / 100
                movement_effectivity += functionality.movement_effectivity * sub_part.destruction_level / 100
                nutrition_effectivity += functionality.nutrition_effectivity * sub_part.destruction_level / 100
                ill_resistance_effectivity += functionality.ill_resistance_effectivity * sub_part.destruction_level / 100

        return PartFunctionality(sight, hands_effectivity, movement_effectivity, nutrition_effectivity, ill_resistance_effectivity)

    def _generate_sub_parts(self):
        sub_parts = self.part.get_sub_part()
        if sub_parts:
            sub_parts_implemetations = list()
            for part in sub_parts:
                sub_parts_implemetations.append(BodyPart(part))
            return sub_parts_implemetations
        return None

    def clean_destruction_level(self):
        self.destruction_level = 0
        for part in self.sub_parts:
            part.destruction_level = 0


def create_human_body():
    result = list()
    for part in _body_parts:
        result.append(BodyPart(part))

    return result
