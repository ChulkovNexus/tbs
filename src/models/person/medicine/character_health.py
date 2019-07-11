from src.models.person.medicine.body_parts import create_human_body
from src.game_mutators.MedicineProcessor import max_blood_count


class CharacterHealth:

    def __init__(self, person):
        self.person = person
        self.sight = 100
        self.hands_effectivity = 100
        self.movement_effectivity = 100
        self.nutrition_effecivity = 100
        self.ill_resistance_effectivity = 100

        self.blood_count = max_blood_count

        self.pain_level = 0
        self.blood_loss_level = 0
        self.body_parts = create_human_body()
        self.injuries = list()

    def refresh_injuries_affects(self):
        self.sight = 100
        self.hands_effectivity = 100
        self.movement_effectivity = 100
        self.nutrition_effecivity = 100
        self.ill_resistance_effectivity = 100

        self.pain_level = 0
        self.blood_loss_level = 0

        for part in self.body_parts:
            part.clean_destruction_level()

        for injury in self.injuries:
            part = next(x for x in self.body_parts if x.part == injury.body_part)
            self.blood_loss_level += injury.blood_loss_level
            self.pain_level += injury.pain_level
            if injury.sub_part:
                sub_part = next(x for x in part.sub_parts if x.part == injury.sub_part)
                sub_part.destruction_level += injury.destruction_level
            else:
                part.destruction_level += injury.destruction_level

        for part in self.body_parts:
            affect = part.get_functionality_affect()

            self.sight -= affect.sight
            self.hands_effectivity -= affect.hands_effectivity
            self.movement_effectivity -= affect.movement_effectivity
            self.nutrition_effecivity -= affect.nutrition_effectivity
            self.ill_resistance_effectivity -= affect.ill_resistance_effectivity
