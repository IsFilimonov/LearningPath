import sys

A = []
actions = (True, )

while len(actions) > 0:
    actions = sys.stdin.readline().strip().split()

    match actions[0]:
        case "push":
            A.append(int(actions[1])) if len(actions) == 2 else ...
            print("ok")

        case "pop":
            # Сначала проверяем на длину массива, чтобы не вызвать исключение
            # Далее проверка на количество параметров в actions
            # Если параметров не 1 --- просто игнорируем
            print(A.pop()) if len(A) > 0 else print("error") if len(actions) == 1 else ... 


        case "back":
            # Важное замечание:
            #   по логике вещей, print(A[-1]) должен выполняться только после 2 проверок if, 
            #   но на практике вызывается исключение IndexError если не проверять длину массива сначала
            #   Ожидаемая логика: 
            #       IF параметры -> IF длина А -> A[-1] -> print
            #   Если сначала проверять количество параметров:
            #       IF параметры -> A[-1] (IndexError)
            #   Поэтому:
            #       IF длина A -> A[-1] -> IF параметры -> print
            # 
            print(A[-1]) if len(A) > 0 else print("error") if len(actions) == 1 else ...

        case "size":
            print(len(A)) if len(actions) == 1 else ...

        case "clear":
            # or оператор выполняет два действия одновременно
            A.clear() or print("ok") if len(actions) == 1 else ...

        case "exit":
            # or оператор выполняет два действия одновременно
            print("bye") or actions.clear() if len(actions) == 1 else ...
