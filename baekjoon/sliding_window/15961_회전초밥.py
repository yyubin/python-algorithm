import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]
left, right = 0, k - 1
dic = defaultdict(int)
ans = -int(1e9)

dic[c] += 1
for i in range(right + 1):
    dic[sushi[i]] += 1

while left < n:
    ans = max(len(dic), ans)
    dic[sushi[left]] -= 1

    if dic[sushi[left]] == 0:
        del dic[sushi[left]]

    left += 1
    right += 1

    dic[sushi[right % n]] += 1

print(ans)

# 답은 나오는데 시간초과
# import sys
# from collections import deque
# import copy
# n, d, k, c = map(int, sys.stdin.readline().split())
# sushi = deque([int(sys.stdin.readline()) for _ in range(n)])
# result = []
# ans = 0
#
# for _ in range(n):
#     tmp = []
#     sushi2 = copy.deepcopy(sushi)
#     while True:
#         if sushi2[0] not in tmp and len(tmp) < k:
#             tmp.append(sushi2[0])
#             sushi2.append(sushi2.popleft())
#         else:
#             if c not in tmp:
#                 ans = max(ans, len(tmp) + 1)
#             else:
#                 ans = max(ans, len(tmp))
#             break
#     sushi.append(sushi.popleft())
#
# print(ans)
