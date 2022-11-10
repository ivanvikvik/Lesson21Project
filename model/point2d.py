import math


class Point2D:
    __count = 0

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def __increment(cls):
        # print("__increment")
        cls.__count += 1

    @classmethod
    def __decrement(cls):
        # print("__decrement")
        cls.__count -= 1

    @staticmethod
    def sum(a, b):
        return a + b

    def __init__(self, x=0, y=0):
        self.__increment()
        self._x = x
        self._y = y

    def __del__(self):
        self.__decrement()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @y.deleter
    def y(self):
        del self._y

    @staticmethod
    def calculate_distance(point1, point2):
        if (not isinstance(point1, Point2D)
                or not isinstance(point2, Point2D)):
            return -1

        return math.sqrt((point1.x - point2.x) ** 2
                         + (point1.y - point2.y) ** 2)

    def distance(self, point):
        return self.calculate_distance(self, point)

    def __str__(self):
        return f"Point ({self._x};{self._y})"
