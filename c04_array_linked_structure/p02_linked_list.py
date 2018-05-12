"""
链表
"""

from numbers import Integral


class LinkedList(object):
    """
    单链表
    """

    class __Node:
        """
        节点
        """

        def __init__(self, data=None, _next=None):
            self.data = data
            self.next = _next

        def __str__(self):
            return str(self.data)

    def __init__(self):
        # 虚拟头节点
        self._dummy_head = self.__Node()
        # 元素个数
        self._size = 0

    @property
    def size(self):
        """
        元素个数
        """

        return self._size

    @property
    def empty(self):
        """
        是否为空
        :return:
        """
        return self._size == 0

    def add(self, index, new_item):
        """
        在链表的index（0-based）位置添加新的元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > self._size:
            raise Exception("Add failed. illegal index.")

        prev = self._dummy_head
        for i in range(index):
            prev = prev.next

        prev.next = self.__Node(new_item, prev.next)
        self._size += 1

    def add_first(self, new_item):
        """
        在链表的头部添加新元素
        """

        return self.add(0, new_item)

    def add_last(self, new_item):
        """
        在链表的末尾添加新元素
        """

        return self.add(self._size, new_item)

    def get(self, index):
        """
        获得链表的index（0-based）个位置的元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > self._size:
            raise Exception("Get failed. illegal index.")

        # 当前节点
        cur = self._dummy_head.next
        for i in range(index):
            cur = cur.next

        return cur.data

    def get_first(self):
        """
        获得链表的第一个元素
        """

        return self.get(0)

    def get_last(self):
        """
        获得链表的最后一个元素
        """
        return self.get(self._size)

    def set(self, index, new_item):
        """
        修改链表的第index（0-based）个位置的元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > self._size:
            raise Exception("Set failed. illegal index.")

        # 当前节点
        cur = self._dummy_head.next
        for i in range(index):
            cur = cur.next

        cur.data = new_item

    def contains(self, item):
        """
        查找链表中是否有元素item
        """

        # 当前节点
        cur = self._dummy_head.next
        while cur is not None:
            if cur.data == item:
                return True

        return False

    def remove(self, index):
        """
        从链表中删除index（0-based）位置的元素，返回删除的元素
        """

        assert isinstance(index, Integral), "index must be int."

        if index < 0 or index > self._size:
            raise Exception("Remove failed. illegal index. ")

        # 前一个节点
        prev = self._dummy_head
        for i in range(index):
            prev = prev.next

        # 需要删除的节点
        remove_node = prev.next
        prev.next = remove_node.next
        remove_node.next = None
        self._size -= 1

        return remove_node.data

    def remove_first(self):
        """
        从链表中删除第一个元素，返回删除的元素
        """

        return self.remove(0)

    def remove_last(self):
        """
        从链表中删除最后一个元素，返回删除的元素
        """

        return self.remove(self._size)

    def remove_element(self, item):
        """
        从链表中删除元素item
        """

        # 之前的节点
        prev = self._dummy_head
        while prev is not None:
            if prev.next.data == item:
                break
            prev = prev.next

        if prev.next is not None:
            remove_node = prev.next
            prev.next = remove_node.next
            remove_node.next = None
            self._size -= 1

    def __iter__(self):
        # 当前节点
        cur = self._dummy_head.next
        while cur is not None:
            yield cur.data
            cur = cur.next

    def __str__(self):
        node_list = list()

        # 当前节点
        cur = self._dummy_head.next
        while cur is not None:
            node_list.append(str(cur) + "->")
            cur = cur.next

        res = "".join(node_list) + "None" if len(node_list) > 0 else "None"
        return res


def use_linked_list():
    linked_list = LinkedList()
    linked_list.add_first("google")
    linked_list.add_first("amazon")
    linked_list.add_last("apple")
    print(linked_list.size)
    print(linked_list.empty)
    print(linked_list)
    linked_list.remove_first()
    print(linked_list)
    print(linked_list.get_first())
    linked_list.remove_element("google")
    print(linked_list)
    # 输出结果：
    """
    3
    False
    amazon->google->apple->None
    google->apple->None
    google
    apple->None
    """


if __name__ == '__main__':
    use_linked_list()
