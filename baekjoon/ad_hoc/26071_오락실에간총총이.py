import sys
n = int(sys.stdin.readline())
r_min, r_max = n, -1
c_min, c_max = n, -1

for i in range(n):
    row = sys.stdin.readline().strip()
    for j, ch in enumerate(row):
        if ch == 'G':
            r_min = min(r_min, i)
            r_max = max(r_max, i)
            c_min = min(c_min, j)
            c_max = max(c_max, j)

def axis_moves(low, high):
    if low == high:
        return 0
    return min(high, (n - 1) - low)

answer = axis_moves(r_min, r_max) + axis_moves(c_min, c_max)
print(answer)


# import sys
# n = int(sys.stdin.readline())
# graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
# bears = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 'G':
#             bears.append((i, j))
#
# def chk(d):
#     tmp_x, tmp_y = 0, 0
#
#     for a, b in bears:
#         tmp_x = max(tmp_x, abs(d[0] - a))
#         tmp_y = max(tmp_y, abs(d[1] - b))
#
#     return tmp_x, tmp_y
#
# res = sys.maxsize
# for i in range(n):
#     for j in range(n):
#         if i == 0:
#             x, y = chk((i, j))
#             res = min(res, x + y)
#         elif j == 0:
#             x, y = chk((i, j))
#             res = min(res, x + y)
# print(res)