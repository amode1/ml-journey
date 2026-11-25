# 1. Вернуть среднее любого числа аргументов; без аргументов — 0
def mean(*args):
    if args == ():
        return 0
    return sum(args)/len(args)

# 2. Вернуть строку "k1=v1, k2=v2" из именованных аргументов в порядке передачи
def format_params(**kwargs):
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())

# 3. Отсортировать студентов (имя, балл) по баллу ↓, при равенстве по имени ↑
def rank(students):
    return sorted(students, key=lambda s: (-s[1], s[0]))

# 4. Транспонировать матрицу (список списков) — одной строкой через zip
def transpose(matrix):
    return [list(x) for x in zip(*matrix)]

# 5. Вернуть функцию, которая умножает на n: make_multiplier(3)(5) == 15
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# 6. Счётчик вызовов: каждый вызов counter() возвращает 1, 2, 3, …
#    Подсказка: вложенная функция + nonlocal
def make_counter():
    x = 0
    def inner():
        nonlocal x
        x += 1
        return x
    return inner
 
assert mean(1, 2, 3) == 2 and mean() == 0
assert format_params(lr=0.1, epochs=5) == "lr=0.1, epochs=5"
assert rank([("Маша", 90), ("Андрей", 95), ("Петя", 90)]) == [("Андрей", 95), ("Маша", 90), ("Петя", 90)]
assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
assert make_multiplier(3)(5) == 15
c = make_counter()
assert c() == 1 and c() == 2 and c() == 3
c2 = make_counter()
assert c2() == 1           # у каждого счётчика своё состояние
print("Все проверки пройдены!")