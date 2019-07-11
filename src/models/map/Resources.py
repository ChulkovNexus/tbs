import itertools

from src.models.items.Item import Item


class Resource(Item):

    def __init__(self):
        super().__init__()
        self.resource_tier = 1
        self.resource_name = type(self).__name__
        self.happynes_multiplyer = 1
        self.strong_multiplyer = 1
        self.nutrien_multiplyer = 1

    def __repr__(self):
        return self.resource_name

class Potatos(Resource):

    def __init__(self):
        super().__init__()


class Corns(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplyer = 1.1


class Wood(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 0.5


class Stone(Resource):

    def __init__(self):
        super().__init__()


class Wool(Resource):

    def __init__(self):
        super().__init__()


class Shugar(Resource):

    def __init__(self):
        super().__init__()
        self.happynes_multiplyer = 1.3
        self.nutrien_multiplyer = 1.1


class Fruits(Resource):

    def __init__(self):
        super().__init__()
        self.happynes_multiplyer = 1.1
        self.nutrien_multiplyer = 1.1


class Pigs(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplyer = 1.3


class Lamb(Resource):

    def __init__(self):
        super().__init__()
        self.nutrien_multiplyer = 1.2


class Strobery(Resource):

    def __init__(self):
        super().__init__()
        self.happynes_multiplyer = 1.2
        self.nutrien_multiplyer = 1.1


class Ambrosia(Resource):

    def __init__(self):
        super().__init__()
        self.happynes_multiplyer = 1.2
        self.nutrien_multiplyer = 1.1


class Metal(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 1.5


class Gold(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 0.5


class Silver(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 0.5


class Spidersilk(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 1.5


class Meefreel(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 2


class Coal(Resource):

    def __init__(self):
        super().__init__()


class Redwood(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 1.3
        self.happynes_multiplyer = 1.3


class Mrecury(Resource):

    def __init__(self):
        super().__init__()


class Plasteel(Resource):

    def __init__(self):
        super().__init__()
        self.strong_multiplyer = 2


first_tier_food_resource = [Potatos(), Corns(), Lamb(), Fruits()]
first_tier_material_resource = [Stone(), Wood(), Metal(), Wool()]
second_tier_food_resource = [Shugar(), Ambrosia(), Strobery()]
second_tier_material_resource = [Coal(), Mrecury(), Redwood(), Plasteel(), Spidersilk(), Silver(), Gold(), Spidersilk()]
third_tier_material_resource = [Meefreel(), Plasteel()]

all_resources = list(itertools.chain(first_tier_food_resource, first_tier_material_resource, second_tier_food_resource, second_tier_material_resource, third_tier_material_resource))
