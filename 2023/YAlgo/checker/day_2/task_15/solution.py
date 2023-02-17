n = int(input())  # количество городов
data = list(map(int, input().split()))  # средняя цена проживания

answer = [-1] * n
b = [0]

for i in range(1, n):
    while len(b) > 0 and data[i] < data[b[-1]]:
        answer[b.pop()] = i
    b.append(i)

print(*answer)
