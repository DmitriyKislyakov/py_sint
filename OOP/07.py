
class TreeObj:
    indx = 0
    def __init__(self, indx, value=None):
        self.value = value
        self.__left = None
        self.__right = None
        self.indx = TreeObj.indx
        TreeObj.indx += 1

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def left(self, value):
        self.__right = value


class DecisionTree:
    def __init__(self, x):
        self.__x = x

    @classmethod
    def predict(cls, root, x):
        pass

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        pass
