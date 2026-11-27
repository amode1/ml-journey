from math import sqrt


class Vector:
    # хранит координаты (любое количество): Vector(1, 2, 3)
    # __repr__  -> "Vector(1, 2, 3)"
    # __len__   -> размерность
    # __getitem__ -> v[i]
    # __eq__
    # __add__, __sub__ -> покоординатно; разные размерности -> ValueError
    #                     не Vector -> NotImplemented
    # __mul__, __rmul__ -> умножение на число (v * 2 и 2 * v)
    # dot(other) -> скалярное произведение: сумма произведений координат
    # norm -> @property, длина вектора: корень из суммы квадратов
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(c) for c in self.coordinates)})"

    def __len__(self):
        return len(self.coordinates)

    def __getitem__(self, key):
        return self.coordinates[key]

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.coordinates == other.coordinates

    def __add__(self, other):
        if not isinstance(other, Vector):
           return NotImplemented
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError
        return Vector(*[self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates))])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError
        return Vector(*[self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates))])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return NotImplemented
        return Vector(*[self.coordinates[i] * other for i in range(len(self.coordinates))])
    
    def __rmul__(self, other):
        if isinstance(other, Vector):
            return NotImplemented
        return Vector(*[self.coordinates[i] * other for i in range(len(self.coordinates))])

    def dot(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError
        return sum([self.coordinates[i] * other.coordinates[i] for i in range(len(self.coordinates))])

    @property
    def norm(self):
        return sqrt(sum(i**2 for i in self.coordinates))
    


    


v = Vector(1, 2, 3)
w = Vector(4, 5, 6)
assert repr(v) == "Vector(1, 2, 3)"
assert len(v) == 3 and v[0] == 1 and v[-1] == 3
assert v + w == Vector(5, 7, 9)
assert w - v == Vector(3, 3, 3)
assert v * 2 == Vector(2, 4, 6) and 2 * v == Vector(2, 4, 6)
assert v.dot(w) == 32
assert Vector(3, 4).norm == 5.0
assert list(v) == [1, 2, 3]             # итерация бесплатно благодаря __getitem__
try:
    v + Vector(1, 2)
    assert False, "должна быть ошибка"
except ValueError:
    pass
print("Все проверки пройдены!")