### >>>>>>
import debugpy
debugpy.listen(5678)
print("Waiting for debugger")
debugpy.wait_for_client()
### <<<<<<
import sys


k = int(sys.stdin.readline().strip())
coo = []
d = {}

for _ in range(k):
    coo.append(tuple(map(int,sys.stdin.readline().strip().split())))

# for run1 in range(0, k):
#     for run2 in range(run1+1, k):
#         # ([X1,Y1],[X2,Y2])
#         key = tuple((coo[run1], coo[run2]))
#         # Геометрическая площадь неверная
#         square = abs(key[0][0] - key[1][0]) * abs(key[0][1] - key[1][1])

#         d[key] = d.get(key, 0) + square

#https: // wiki5.ru/wiki/Minimum_bounding_rectangle
# min x min y max x max y
# через zip

print("Done!")