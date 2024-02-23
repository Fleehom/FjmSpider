from copy import deepcopy
from pprint import pformat
from collections.abc import MutableMapping
from bald_spider.items import Field, ItemMeta
from bald_spider.exceptions import ItemInitError, ItemAttributeError


class Item(MutableMapping, metaclass=ItemMeta):

    FIELDS: dict = dict()

    def __init__(self, *args, **kwargs):
        self._values = {}
        if args:
            raise ItemInitError(f"{self.__class__.__name__}: position args is not supported, use keyword args.")
        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __setitem__(self, key, value):
        if key in self.FIELDS:
            self._values[key] = value
        else:
            raise KeyError(f"{self.__class__.__name__} doesn't support field: {key}")

    def __getitem__(self, item):
        return self._values[item]

    def __delitem__(self, key):
        del self._values[key]

    def __setattr__(self, key, value):
        if not key.startswith('_'):
            raise AttributeError(f"use item[{key!r}] = {value!r} to set field value.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        raise AttributeError(
            f"{self.__class__.__name__} doesn't support field: {item}, "
            f"please add the `{item}` field to the {self.__class__.__name__}, "
            f"and use item[{item!r}] to get field value."
        )

    def __getattribute__(self, item):
        field = super().__getattribute__('FIELDS')
        if item in field:
            raise ItemAttributeError(f"use item[{item!r}] to set field value.")
        else:
            return super().__getattribute__(item)

    def __repr__(self):
        return pformat(dict(self))

    __str__ = __repr__

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)

    def to_dict(self):
        return dict(self)

    def copy(self):
        return deepcopy(self)


if __name__ == '__main__':
    class TestItem(Item):
        url = Field()
        title = Field()

    class TestItem2(Item):
        name = Field()

    test_item = TestItem(url='22222')
    # test_item['url'] = '11111111111'
    print(test_item['url'])