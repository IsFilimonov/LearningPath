import sys
from collections import deque

# Варианты стека в Python:
# list (оптимизирован для быстрых операций с фиксированной длиной): append, pop T: O(n)
# deque (обобщение стеков и очередей): быстрые append, pop T: O(1) в любом направлении
# queue: тоже имеет LIFO
# linked list


def check_sequence(text: str) -> bool:
    """Проверка правильности скобочной последовательности.

    Последователость состоит из 3 видов скобок (), [], {}.

    Args:
        text (str): последовательность скобок.

    Returns:
        bool: результат проверки: правильная или нет.
    """
    stack = deque()
    # keys: open
    # values: closed
    d = {"(": ")", "[": "]", "{": "}"}

    # Нулевая последовательность = Правильная последовательность
    if len(text) == 0:
        return True  
    
    for char in text:
        # Последовательность не должна начинаться с close скобки
        if len(stack) == 0 and char in d.values():
            return False
        
        # Open скобка
        if char in d.keys():
            stack.append(char)
        elif char in d.values():
            last = stack[-1]
            if d[last] == char:
                stack.pop()
            else:
                return False
            
    # В конце стек должен быть пустым
    return True if len(stack) == 0 else False

data = sys.stdin.readline().strip()
print("yes" if check_sequence(data) else "no")

