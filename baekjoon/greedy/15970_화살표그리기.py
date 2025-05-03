import sys
from collections import defaultdict
n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
color_map = defaultdict(list)

for x, c in points:
    color_map[c].append(x)
res = 0

for color, x_list in color_map.items():
    x_list.sort()
    for i in range(len(x_list)):
        if len(x_list) == 1:
            continue
        if i == 0:
            res += abs(x_list[1] - x_list[0])
        elif i == len(x_list) - 1:
            res += abs(x_list[-1] - x_list[-2])
        else:
            res += min(abs(x_list[i] - x_list[i-1]), abs(x_list[i+1] - x_list[i]))

print(res)

