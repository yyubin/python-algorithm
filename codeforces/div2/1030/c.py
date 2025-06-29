import sys
from collections import deque
import heapq
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    bit = [bin(i).count('1') for i in a]
    q = list()
    for i in a:
        s = bin(i)[2:]
        for j in range(len(s)):
            if s[-1-j] == '0':
                cost = 2 ** j - (i % (2 ** (j + 1)))
                q.append((cost, i))
                break
        else:
            next_pow2 = 1 << len(s)
            cost = next_pow2 - i
            q.append((cost, i))
    heapq.heapify(q)
    while k and q:
        cost, i = heapq.heappop(q)
        if cost > k:
            break
        k -= cost
        bit[i] += 1
        a[i] += cost

        next_cost = ...
        heapq.heappush(q, (next_cost, i))
    print(q)