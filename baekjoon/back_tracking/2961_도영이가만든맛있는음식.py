import sys
from itertools import combinations
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

com = []
for i in range(1, n+1):
    com.append(combinations(li, i))

result = sys.maxsize

for i in com:
    for j in i:
        a, b = 1, 0
        for c in j:
            a *= c[0]
            b += c[1]
        result = min(result, abs(a - b))

print(result)



