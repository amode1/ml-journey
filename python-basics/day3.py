from collections import Counter, defaultdict

# 1. Вернуть True, если s и t — анаграммы (одинаковые буквы в одинаковом количестве)
#    Сделайте БЕЗ Counter и без сортировки — словарём
def is_anagram(s, t):
    s1 = {}
    t1 = {}
    for i in s:
        s1[i] = s1.get(i, 0) + 1
    for i in t:
        t1[i] = t1.get(i, 0) + 1
    return s1 == t1

# 2. Вернуть первый символ, который встречается в строке ровно 1 раз, иначе ""
def first_unique_char(s):
    s1 = {}
    for i in s:
        s1[i] = s1.get(i, 0) + 1
    for ch in s:
        if s1[ch] == 1:
            return ch
    return ""

# 3. Сгруппировать слова по первой букве: {'a': ['apple', 'avocado'], 'b': ['banana']}
def group_by_first_letter(words):
    groups = {}
    for i in words:
        key = i[0]
        groups.setdefault(key, []).append(i)
    return groups

# 4. Вернуть индексы двух чисел с суммой target за O(n) (гарантируется, что решение есть)
def two_sum(nums, target):
    pos = {}
    for i , j in enumerate(nums):
        if target - j in pos:
            return [pos[target - j], i]
        pos[j] = i

# 5. Вернуть k самых частых слов в тексте (при равной частоте — в порядке первого появления)
def top_k_words(text, k):
    chastota = {}
    first_pos = {}

    words = text.split()
    for idx, w in enumerate(words):
        chastota[w] = chastota.get(w, 0) + 1
        if w not in first_pos:
            first_pos[w] = idx

    ordered = sorted(chastota.keys(), key=lambda w: (-chastota[w], first_pos[w]))
    return ordered[:k]
    

assert is_anagram("listen", "silent") and not is_anagram("rat", "car")
assert not is_anagram("aab", "abb")
assert first_unique_char("leetcode") == "l"
assert first_unique_char("loveleetcode") == "v"
assert first_unique_char("aabb") == ""
assert group_by_first_letter(["apple", "banana", "avocado"]) == {"a": ["apple", "avocado"], "b": ["banana"]}
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert (top_k_words("a b a c b a", 2)) == ["a", "b"]
print("Все проверки пройдены!")
