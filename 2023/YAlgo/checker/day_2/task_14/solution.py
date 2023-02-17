from collections import deque

def ckeck_train(way1: list[int]) -> bool:
    """Проверка возможности сортировки состава поезда по порядку.

    Args:
        way1 (list[int]): состав поезда на 1 пути (HEAD-в-разнобой-999).

    Returns:
        bool: возможно или нет отсортировать состав?
    """

    ready = 1  # номер готового к парковке вагона на 2 путь
    deadlock = deque()  # тупик
    way2 = deque()  # состав поезда на 2 пути из тупика: 1-2-3-HEAD

    while len(way1) > 0:
        # перевозим вагоны с 1 пути -> тупик 
        deadlock.append(way1.popleft())

        while len(deadlock) > 0 and deadlock[-1] == ready:
            # условие проверки длины необходимо, чтобы не вызывать list index out of range
            # перевозим вагоны из тупика -> 2 путь
            way2.append(deadlock.pop())
            ready += 1

    return True if len(way1) == 0 and len(deadlock) == 0 else False


n = int(input())
data = deque(map(int, input().split()))

print("YES" if ckeck_train(data) else "NO")
