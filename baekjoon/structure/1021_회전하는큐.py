import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
q = [i + 1 for i in range(n)]

cnt = 0
for i in li:
    if q[0] == i:
        q.pop(0)
        continue

    if q.index(i) > len(q)//2:
        for j in range(q.index(i), len(q)):
            q.insert(0, q.pop())
            cnt += 1
        q.pop(0)
    else:
        for j in range(q.index(i)):
            q.append(q.pop(0))
            cnt += 1
        q.pop(0)

print(cnt)
