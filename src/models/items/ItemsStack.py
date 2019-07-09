from src.models.items import Item


class ItemsStack:

    def __init__(self):
        self._items = {}

    def add_item(self, item: Item, add_count=1):
        count = self._items[item.type] or 0
        self._items[item.type] = count + add_count

    def remove(self, item: Item, remove_count=1):
        count = self._items[item.type] or 0
        if count < remove_count:
            raise ValueError('not enough items in items stack')
        else:
            self._items[item.type] = count - remove_count

        if self._items[item.type] == 0:
            del self._items[item.type]

    def move_item(self, item: Item, to_items_stack, move_count: int):
        self.remove(item, move_count)
        to_items_stack.add_item(item, move_count)
