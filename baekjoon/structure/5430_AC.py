import sys
from collections import deque
tc = int(sys.stdin.readline())

for _ in range(tc):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    li = input()[1:-1].split(',')

    q = deque(li)
    flag = 0

    if n == 0:
        q = []

    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(q) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")

