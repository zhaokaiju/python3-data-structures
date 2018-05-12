"""
基于数组实现的包
"""

from c04_array_linked_structure.p01_array import Array


class ArrayBag(object):
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        self._items = Array(self.DEFAULT_CAPACITY)
        if source_collection:
            for item in source_collection:
                self._items.add_last(item)

    def is_empty(self):
        return self._items.empty

    def __len__(self):
        return self._items.size

    def __str__(self):
        if self.is_empty():
            return "{}"

        return "{" + " ,".join([str(item) for item in self._items if item is not None]) + "}"

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result._items.add_last(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True

        if type(self) != type(other) or len(self) != len(other):
            return False

        for item in self:
            if item not in other:
                return False

        return True

    def clear(self):
        self._items = Array(self.DEFAULT_CAPACITY)

    def add(self, new_item):
        self._items.add_last(new_item)

    def remove(self, item):
        return self._items.remove(item)


def use_array_bag():
    array_bag = ArrayBag([1, 3, 2])
    array_bag.add(4)
    array_bag += array_bag
    array_bag.remove(3)
    print(array_bag)
    print(array_bag.is_empty())
    print(len(array_bag))

    item_list = [item for item in array_bag if item is not None]
    print(item_list)

    array_bag_other = ArrayBag([1, 3, 2])
    print(array_bag == array_bag_other)
    array_bag_other.clear()
    print(array_bag_other)
    # 输出结果：
    """
    {1 ,3 ,2 ,1 ,3 ,2 ,4}
    False
    7
    [1, 3, 2, 1, 3, 2, 4]
    False
    {}
    """


if __name__ == '__main__':
    use_array_bag()
