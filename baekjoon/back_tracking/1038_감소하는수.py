import sys
from itertools import combinations

n = int(sys.stdin.readline())
result = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        result.append(int("".join(map(str, num))))

result.sort()
print(result[n] if len(result) > n else -1)


## https://fre2-dom.tistory.com/487
