import sys

def solve(text: str) -> int:
    """Решение выражения в постфиксной записе.

    Args:
        text (str): постфиксная запись

    Returns:
        int: результат выражения
    """
    stack = []

    for el in text:
        if el.isdigit():
            stack.append(int(el))
            continue

        y = stack.pop()
        x = stack.pop()
        z = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y
            }[el](x, y)
        
        stack.append(z)

    return stack.pop()


data = input().split()

print(solve(data))
