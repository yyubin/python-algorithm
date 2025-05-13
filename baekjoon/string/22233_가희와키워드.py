import sys
n, m = map(int, sys.stdin.readline().split())
memo = {}
res = 0
for _ in range(n):
    memo[sys.stdin.readline().rstrip()] = 1
    res += 1
for _ in range(m):
    li = sys.stdin.readline().rstrip().split(',')
    for i in li:
        if i in memo:
            res -= 1
            del memo[i]
    print(res)


# set 보다 dict 이 시간복잡도에서 유리
# import sys
# n, m = map(int, sys.stdin.readline().split())
# memo = {sys.stdin.readline().rstrip() for _ in range(n)}
# blog = set()
# for _ in range(m):
#     li = sys.stdin.readline().rstrip().split(',')
#     for i in li:
#         if i in memo:
#             memo.remove(i)
#     print(len(memo))
