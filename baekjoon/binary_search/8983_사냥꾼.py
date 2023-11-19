import sys
m, n, l = map(int, sys.stdin.readline().split())
spot = list(map(int, sys.stdin.readline().split()))
animals = list(map(int, sys.stdin.readline().split()) for _ in range(n))

spot.sort()
result = 0

for x, y in animals:
    if y > l:
        continue

    max_ = x+y-l
    min_ = x-y+l
    left, right = 0, m-1

    while left <= right:
        mid = (left+right)//2
        if max_ <= spot[mid] <= min_:
            result += 1
            break
        elif spot[mid] < min_:
            left = mid + 1
        else:
            right = mid - 1

print(result)
## 23
# import sys
# m, n, l = map(int, sys.stdin.readline().split())
# spot = list(map(int, sys.stdin.readline().split()))
#
# animals = []
# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     animals.append((a, b))
#
# visited = [False for _ in range(n)]
#
# def check_animals(x1, x2, y):
#     for j in range(n):
#         if not visited[j] and animals[j][1] == y and x1 <= animals[j][0] <= x2:
#             visited[j] = True
#
# for i in spot:
#     x1 = i-l
#     x2 = i+l
#     y = 0
#
#     for _ in range(l+1):
#         check_animals(x1, x2, y)
#         y += 1
#         x1 += 1
#         x2 -= 1
#
# print(visited.count(True))








