import sys

# n, k, row, column = int(input()), int(input()), int(input()), int(input())
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
row = int(sys.stdin.readline().strip())
line = int(sys.stdin.readline().strip())

pos1 = (row - 1) * 2 + line - k
pos2 = (row - 1) * 2 + line + k
row1 = (pos1 + 1) // 2
row2 = (pos2 + 1) // 2

if pos1 > 0 and (pos2 > n or abs(row - row1) < abs(row - row2)):
    print(row1, 2 - pos1 % 2)
elif pos2 <= n:
    print(row2, 2 - pos2 % 2)
else:
    print(-1)
