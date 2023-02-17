import sys


N = int(sys.stdin.readline().strip())
if N > 0:
    V = list(map(int, sys.stdin.readline().split()))
    V.sort()
else:
    next(sys.stdin)
    
C = int(sys.stdin.readline().strip())
if C > 0:
    P = list(map(int, sys.stdin.readline().split()))
    for collector_min in P:
        cnt = 0
        for el_id in V:
            if el_id < collector_min:
                cnt += 1

        print(cnt)
