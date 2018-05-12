"""
基于链表实现的包
"""

from c04_array_linked_structure.p02_linked_list import LinkedList


class LinkedListBag(object):
    """
    基于链表实现的包
    """

    def __init__(self, source_collection=None):
        self._items = LinkedList()
        if source_collection:
            for item in source_collection:
                self.add(item)

    def is_empty(self):
        return self._items.empty

    def __len__(self):
        return self._items.size

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        return iter(self._items)

    def __add__(self, other):
        result = LinkedListBag(self)
        for item in other:
            result.add(item)
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
        self._items = LinkedList()

    def add(self, item):
        self._items.add_last(item)

    def remove(self, item):
        self._items.remove_element(item)


def use_linked_list_bag():
    bag = LinkedListBag([1, 3, 2])
    bag.add(4)
    bag += bag
    bag.remove(3)
    print(bag)
    print(bag.is_empty())
    print(len(bag))

    item_list = []
    for item in bag:
        item_list.append(item)
    print(item_list)

    bag_other = LinkedListBag([1, 3, 2])
    print(bag == bag_other)
    bag_other.clear()
    print(bag_other)
    # 输出结果：
    """
    {1, 2, 4, 1, 3, 2, 4}
    False
    7
    [1, 2, 4, 1, 3, 2, 4]
    False
    {}
    """


if __name__ == '__main__':
    use_linked_list_bag()
