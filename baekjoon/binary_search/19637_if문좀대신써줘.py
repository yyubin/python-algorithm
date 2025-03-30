import sys
n, m = map(int, sys.stdin.readline().split())
li = []
s = set()
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b not in s:
        li.append((a, int(b)))
        s.add(b)
li.sort(key=lambda x: x[1])
users = [int(sys.stdin.readline()) for _ in range(m)]

for i in range(m):
    start, end = 0, len(li)-1
    tmp = 0
    while start <= end:
        mid = (start + end) // 2
        if li[mid][1] < users[i]:
            start = mid + 1
        elif li[mid][1] > users[i]:
            end = mid - 1
            tmp = li[mid][0]
        else:
            tmp = li[mid][0]
            break
    print(tmp)



# 그냥 구현이 아니라 이분탐색이었음 범위 10^5
# import sys
# n, m = map(int, sys.stdin.readline().split())
# title = dict()
#
# for _ in range(n):
#     a, b = map(str, sys.stdin.readline().split())
#     if int(b) not in title:
#         title[int(b)] = a
#
# users = [int(sys.stdin.readline()) for _ in range(m)]
# title = dict(sorted(title.items(), key=lambda x: x))
#
# for i in users:
#     for j, v in title.items():
#         if i <= j:
#             print(v)
#             break
#
