"""
包接口
"""


class BagInterface(object):
    """
    包接口
    """

    def __init__(self, source_collection=None):
        pass

    def is_empty(self):
        return True

    def __len__(self):
        return 0

    def __str__(self):
        return ""

    def __iter__(self):
        return None

    def __add__(self, other):
        return None

    def __eq__(self, other):
        return None

    def clear(self):
        pass

    def add(self, new_item):
        pass

    def remove(self, item):
        pass
