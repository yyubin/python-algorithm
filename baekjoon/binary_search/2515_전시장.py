import bisect
import sys
n, s = map(int, sys.stdin.readline().split())
pictures = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
heights = [0]
d = [0]
pictures.sort()

for h, c in pictures:
    target = h - s
    idx = bisect.bisect_right(heights, target) - 1
    best = d[idx] + c

    d.append(max(d[-1], best))
    heights.append(h)

print(d[-1])

# for i in range(1, n+1):
#     if pictures[i][0] - pictures[i-1][0] >= s:
#         d[i] = d[i-1] + pictures[i][1]
#     else:
#         idx = bisect.bisect_left(pictures, (pictures[i][0]-s, 0))
#         d[i] = max(d[i-1], d[idx-1] + pictures[i][1])
#
# print(d[-1])
#
#

