import sys
n, l = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def check(li):
    for i in range(n-1):
        if li[i] == li[i+1]:
            continue
        if abs(li[i] - li[i+1]) > 1:
            return False
        if li[i] > li[i+1]:
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if li[i+1] != li[j]:
                        return False
                    if tmp[j]:
                        return False
                    tmp[j] = True
                else:
                    return False
        else:
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if li[i] != li[j]:
                        return False
                    if tmp[j]:
                        return False
                    tmp[j] = True
                else:
                    return False

    return True


result = 0
for k in graph:
    tmp = [False] * n
    if check(k):
        result += 1

for k in range(n):
    tmp = [False] * n
    if check([graph[j][k] for j in range(n)]):
        result += 1

print(result)



# import sys
# n, l = map(int, sys.stdin.readline().split())
#
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# result = 0
# for i in range(n):
#     tmp_max = max(graph[i])
#     tmp_min = min(graph[i])
#     if tmp_max == tmp_min:
#         result += 1
#         continue
#
#     tmp = [False] * n
#     ans = True
#     for j in range(n-1):
#         if graph[i][j] == graph[i][j+1]:
#             continue
#         if abs(graph[i][j] == graph[i][j+1]) > 1:
#             ans = False
#
#         if graph[i][j] > graph[i][j+1]:
#             for k in range(j+1, j+1+l):
#                 if 0 <= k < n:
#                     if graph[i][j+1] != graph[i][k]:
#                         ans = False
#                     if tmp[k]:
#                         ans = False
#                     tmp[k] = True
#                 else:
#                     ans = False
#         else:
#             for k in range(j, j-l, -1):
#                 if 0 <= k < n:
#                     if graph[i][j+1] != graph[i][k]:
#                         ans = False
#                     if tmp[k]:
#                         ans = False
#                     tmp[k] = True
#                 else:
#                     ans = False
#     if ans:
#         result += 1
#
# print(result)
#
#
#
#
