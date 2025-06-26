import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right
n = int(sys.stdin.readline())
x_dict = defaultdict(list)
y_dict = defaultdict(list)
trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
tree_dic = defaultdict(int)
for x, y in trees:
    x_dict[x].append(y)
    y_dict[y].append(x)
    tree_dic[(x, y)] += 1

for ys in x_dict.values():
    ys.sort()

for xs in y_dict.values():
    xs.sort()

for _ in range(int(sys.stdin.readline())):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    cnt = 0
    ys1 = x_dict[x1]
    cnt += bisect_right(ys1, y2) - bisect_left(ys1, y1)
    ys2 = x_dict[x2]
    cnt += bisect_right(ys2, y2) - bisect_left(ys2, y1)
    xs1 = y_dict[y1]
    cnt += bisect_right(xs1, x2) - bisect_left(xs1, x1)
    xs2 = y_dict[y2]
    cnt += bisect_right(xs2, x2) - bisect_left(xs2, x1)

    corner = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    for c in corner:
        cnt -= tree_dic[c]
    print(cnt)


# 성능 안나옴 최대 30억이라 안됨
# import sys
# from bisect import bisect_left, bisect_right
# n = int(sys.stdin.readline())
# x_tree = []
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     x_tree.append((x, y))
# x_tree.sort()
# for _ in range(int(sys.stdin.readline())):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     left = bisect_left(x_tree, (x1, y1))
#     right = bisect_right(x_tree, (x2, y2))
#     cnt = 0
#     for x, y in x_tree[left:right]:
#         if y1 <= y <= y2 and (x == x1 or x == x2):
#             cnt += 1
#         elif x1 <= x <= x2 and (y == y1 or y == y2):
#             cnt += 1
#     print(cnt)
#
