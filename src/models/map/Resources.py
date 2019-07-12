import itertools

from src.models.items.Item import Item


class Resource(Item):

    def __init__(self):
        super().__init__()
        self.resource_tier = 1
        self.resource_name = type(self).__name__
        self.happiness_multiplier = 1
        self.strong_multiplier = 1
        self.nutrien_multiplier = 1

    def __repr__(self):
        return self.resource_name


class Potatos(Resource):

    def __init__(self):
        super().__init__()


class Corns(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplier = 1.1


class Wood(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplier = 0.5


class Sand(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplier = 0.5


class Stone(Resource):

    def __init__(self):
        super().__init__()


class Wool(Resource):

    def __init__(self):
        super().__init__()


class Shugar(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.happynes_multiplier = 1.3
        self.nutrien_multiplier = 1.1


class Fruits(Resource):

    def __init__(self):
        super().__init__()
        self.happynes_multiplier = 1.1
        self.nutrien_multiplier = 1.1


class Pigs(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplier = 1.3


class Lamb(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplier = 1.2


class Strobery(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.happynes_multiplier = 1.2
        self.nutrien_multiplier = 1.1


class Hop(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2


class Ambrosia(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.happynes_multiplier = 1.2
        self.nutrien_multiplier = 1.1


class Metal(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplier = 1.5


class Gold(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.strong_multiplier = 0.5


class Silver(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.strong_multiplier = 0.5


class Spidersilk(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.strong_multiplier = 1.5


class Meefreel(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 3
        self.strong_multiplier = 2


class Coal(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2


class Redwood(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2
        self.strong_multiplier = 1.3
        self.happiness_multiplier = 1.3


class Mercury(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 2


class Plasteel(Resource):

    def __init__(self):
        super().__init__()
        self.resource_tier = 3
        self.strong_multiplier = 2


first_tier_food_resource = [Potatos(), Corns(), Lamb(), Fruits()]
first_tier_material_resource = [Stone(), Wood(), Metal()]
second_tier_food_resource = [Shugar(), Ambrosia(), Strobery(), Hop(), Sand(), Wool()]
second_tier_material_resource = [Coal(), Mercury(), Redwood(), Spidersilk(), Silver(), Gold()]
third_tier_material_resource = [Meefreel(), Plasteel()]

all_resources = list(itertools.chain(first_tier_food_resource, first_tier_material_resource, second_tier_food_resource, second_tier_material_resource, third_tier_material_resource))
