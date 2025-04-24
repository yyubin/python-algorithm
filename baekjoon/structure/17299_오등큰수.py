import sys
from collections import defaultdict
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)
res = [-1] * n
stack = []

for i in li:
    dic[i] += 1

for i in range(n-1, -1, -1):
    while stack and dic[li[i]] >= dic[li[stack[-1]]]:
        stack.pop()
    if stack:
        res[i] = li[stack[-1]]
    stack.append(i)

print(*res)

# 각 원소 Ai에 대해 오른쪽에 있으면서 등장 횟수가 F(Ai)보다 큰 값 중 가장 왼쪽 값
# 등장 횟수 세기: O(N)
# 한 번의 순회 + 스택 push/pop: O(N)