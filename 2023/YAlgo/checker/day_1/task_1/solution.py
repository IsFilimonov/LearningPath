import sys
from collections import OrderedDict
from itertools import zip_longest

input = sys.stdin.read().strip()

# frequency table -- Таблица частот
ft = {}

# Заполнение таблицы частот
for char in input:
    if char != " " and char != "\n":
        ft[char] = ft.get(char, "") + "#"

# Сортировка по ключам
od = OrderedDict(sorted(ft.items()))

# Высвобождение памяти
del OrderedDict

# Заполнение пустых значений с помощью zip_longest и обратный ход
for row in tuple(zip_longest(*od.values(), fillvalue=" "))[::-1]:
    print("".join(row))

# Высвобождение памяти
del zip_longest

# Последовательность ключей
print("".join(od.keys()))
