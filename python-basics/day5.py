class Person:
    # name, age; метод introduce() -> "Я <name>, мне <age>"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Я {self.name}, мне {self.age}'

class Student(Person):
    # + group и grades (список оценок, по умолчанию ПУСТОЙ — помните ловушку!)
    # add_grade(g), average() -> 0 если оценок нет
    # introduce() дополняет родительский: "Я <name>, мне <age>, группа <group>"
    # __str__ -> "<name> (<average с 2 знаками после запятой>)"
    def __init__(self, name, age, group, grades=None):
        super().__init__(name, age)
        self.group = group
        self.grades = list(grades) if grades is not None else []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)

    def introduce(self):
        return super().introduce() + f', группа {self.group}'

    def __str__(self):
        return f'{self.name} ({self.average():.2f})'

class Group:
    # композиция: name, список студентов
    # add(student), __len__, best_student() -> студент с max средним (None, если пусто)
    # average() -> среднее средних по группе (0, если пусто)
    def __init__(self, name):
        self.name = name
        self.students = []

    def add(self, student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def best_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())

    def average(self):
        if not self.students:
            return 0
        return sum(x.average() for x in self.students) / len(self.students)



a = Student("Андрей", 19, "НКАбд-01-25")
m = Student("Маша", 20, "НКАбд-01-25")
for g in [5, 4, 5]: a.add_grade(g)
for g in [5, 5]: m.add_grade(g)

assert a.introduce() == "Я Андрей, мне 19, группа НКАбд-01-25"
assert Person("Петя", 30).introduce() == "Я Петя, мне 30"
assert str(a) == "Андрей (4.67)"
assert Student("Новый", 18, "X").average() == 0
assert Student("Новый", 18, "X").grades == []        # у каждого свой список
assert isinstance(a, Person)

g = Group("НКАбд-01-25")
assert len(g) == 0 and g.best_student() is None and g.average() == 0
g.add(a); g.add(m)
assert len(g) == 2
assert g.best_student() is m
assert round(g.average(), 2) == 4.83
print("Все проверки пройдены!")