"""
数组（动态数组）
"""

from numbers import Integral


class Array(object):
    """
    数组（基于list实现）
    """

    def __init__(self, capacity=10, fill_value=None):
        self._items = list()
        for i in range(capacity):
            self._items.append(fill_value)
        self._size = 0
        self._fill_value = fill_value

    def __len__(self):
        """
        物理大小（容量）
        """

        return len(self._items)

    @property
    def capacity(self):
        """
        物理大小（容量）
        """

        return len(self._items)

    @property
    def size(self):
        """
        逻辑大小（数组元素个数）
        """

        return self._size

    @property
    def empty(self):
        """
        是否为空
        """

        return self._size == 0

    def __str__(self):
        res = "Array: size = {size}, capacity = {capacity}\n".format(size=self._size, capacity=self.__len__())
        res += "["

        if self._size > 0:
            res += ", ".join([str(item) for item in self._items[0: self._size]])

        res += "]"
        return res

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        """
        获取index索引位置的元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > len(self._items):
            raise Exception("Get failed. index is illegal.")

        return self._items[index]

    def __setitem__(self, index, new_item):
        """
        修改index索引位置的元素为new_item
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > len(self._items):
            raise Exception("Set failed. index is illegal.")

        self._items[index] = new_item

    def add(self, index, new_item):
        """
        向指定的位置添加元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > len(self._items):
            raise Exception("Add failed. Require index >=0 and index <= size.")

        # 查看容量是否足够，否则进行扩容
        if self._size == len(self._items):
            # 扩容2倍
            self.__resize(2 * len(self._items))

        # 从最后开始进行数据复制
        i = self._size - 1
        while i >= index:
            self._items[i + 1] = self._items[i]
            i -= 1

        self._items[index] = new_item
        self._size += 1

    def __resize(self, new_capacity):
        """
        扩容/缩容
        """

        new_items = [self._fill_value for _ in range(new_capacity)]
        for i in range(self._size):
            new_items[i] = self._items[i]

        self._items = new_items

    def add_first(self, new_item):
        """
        向所有元素头添加一个新元素
        """

        self.add(0, new_item)

    def add_last(self, new_item):
        """
        向所有元素后添加一个新元素
        """

        self.add(self._size, new_item)

    def get_first(self):
        """
        获取第一个元素
        """

        return self.__getitem__(0)

    def get_last(self):
        """
        获取最后一个元素
        """

        return self.__getitem__(self._size - 1)

    def __contains__(self, item):
        """
        查找数组中是否有元素item
        """
        return item in self._items

    def find(self, item):
        """
        查找数组中元素item所在的索引，如果不存在元素item，则返回-1
        """

        for i in range(self._size):
            if self._items[i] == item:
                return i

        return -1

    def remove(self, index):
        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > self._size:
            raise Exception("Remove failed. Require index >=0 and index <= size.")

        res = self._items[index]

        # 将数组后面的值复制到前面
        for i in range(index + 1, self._size):
            self._items[i - 1] = self._items[i]

        self._size -= 1
        # 处理闲散对象
        self._items[self._size] = self._fill_value

        # 解决复杂震荡（当size == capacity / 4 时，才将capacity减半））
        if self._size == len(self._items) // 4 and len(self._items) // 2 != 0:
            self.__resize(len(self._items) // 2)

        return res

    def remove_first(self):
        """
        从数组中删除第一个元素，返回删除的元素
        """

        return self.remove(0)

    def remove_last(self):
        """
        从数组中删除最后一个元素，返回删除的元素
        """

        return self.remove(self._size - 1)

    def remove_element(self, item):
        """
        从数组中删除元素item
        """

        index = self.find(item)
        if index != -1:
            self.remove(index)

    def swap(self, i, j):
        """
        交换位置
        """

        assert isinstance(i, Integral) and isinstance(j, Integral), "index must be int."

        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise Exception("index is illegal.")

        self._items[i], self._items[j] = self._items[j] = self._items[i]


def use_array():
    array = Array()
    for i in range(3):
        array.add_last(i)

    array.add_first(12)
    print(array)
    # 输出结果：
    """
    Array: size = 4, capacity = 10
    [12, 0, 1, 2]
    """

    print(array.size)
    print(len(array))
    print(array.empty)
    print(array.get_first())
    print(array.get_last())
    array.__setitem__(1, 168)
    print(array.__contains__(168))
    print(array.find(168))
    print(array)
    # 输出结果：
    """
    4
    10
    False
    12
    2
    True
    1
    Array: size = 4, capacity = 10
    [12, 168, 1, 2]
    """

    print(array.remove_last())
    print(array.remove_first())
    print(array.remove_element(168))
    print(array)
    # 输出结果：
    """
    2
    12
    None
    Array: size = 1, capacity = 2
    [1]
    """


if __name__ == '__main__':
    use_array()
