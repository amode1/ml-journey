# 1. Вернуть список без дубликатов, СОХРАНИВ порядок первого появления
def unique_keep_order(nums):
    seen = set()
    uniq = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq

# 2. Вернуть True, если строка — палиндром (без учёта регистра и пробелов)
def is_palindrome(s):
    copy_s = s[:].lower().replace(' ','')
    return copy_s[::-1] == copy_s

# 3. Вернуть самое длинное слово в предложении (при равенстве — первое)
def longest_word(sentence):
    a = sentence.split(' ')
    max_word = ''
    for i in a:
        if len(max_word) < len(i):
            max_word = i
    return max_word

# 4. Вернуть отсортированный список элементов, общих для двух списков (без повторов)
def common(a, b):
    return sorted(set(a) & set(b))

# 5. Повернуть список на k шагов вправо: [1,2,3,4,5], k=2 → [4,5,1,2,3]
def rotate(nums, k):
    if not nums:
        return nums
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]



assert unique_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
assert is_palindrome("А роза упала на лапу Азора")
assert not is_palindrome("python")
assert longest_word("I love machine learning") == "learning"
assert longest_word("ab cd") == "ab"
assert common([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate([1, 2, 3], 3) == [1, 2, 3]
assert rotate([1, 2, 3], 5) == [2, 3, 1]
print("Все проверки пройдены!")