# 1. Вернуть сумму двух чисел
def add(a, b):
    return a+b

# 2. Вернуть "even", если n чётное, иначе "odd"
def parity(n):
    return 'even' if n % 2 == 0 else 'odd'

# 3. Вернуть наибольшее из трёх чисел, НЕ используя max()
def max3(a, b, c):
    best = a
    if b > best:
        best = b
    if c > best:
        best = c
    return best

# 4. Вернуть сумму чисел от 1 до n включительно (циклом)
def sum_to(n):
    summator = 0
    for i in range(n + 1):
        summator += i
    return summator

# 5. Вернуть количество гласных (aeiou) в строке s (строчные буквы)
def count_vowels(s):
    counter = 0
    for i in s:
        if i in ['a','e','i','o','u']:
            counter += 1
    return counter

# 6. Вернуть строку задом наперёд
def reverse(s):
    return s[::-1]

# 7. Вернуть новый список только из чётных чисел списка nums
def evens(nums):
    return [i for i in nums if i % 2 == 0]

# 8. Вернуть словарь: буква -> сколько раз встречается в s
def char_count(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# 9. Вернуть True, если n простое (делится только на 1 и себя), иначе False
def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# 10. Вернуть f-строку вида "Андрей, 19 лет" по имени и возрасту
def greet(name, age):
    return f'{name}, {age} лет'


# --- проверки: не меняйте ---
assert add(2, 3) == 5
assert parity(4) == "even" and parity(7) == "odd"
assert max3(1, 9, 4) == 9 and max3(-1, -5, -3) == -1
assert sum_to(1) == 1 and sum_to(100) == 5050
assert count_vowels("machine learning") == 6
assert reverse("numpy") == "ypmun"
assert evens([1, 2, 3, 4, 10]) == [2, 4, 10]
assert char_count("abca") == {"a": 2, "b": 1, "c": 1}
assert is_prime(2) and is_prime(13) and not is_prime(1) and not is_prime(15)
assert greet("Андрей", 19) == "Андрей, 19 лет"
print("Все проверки пройдены!")