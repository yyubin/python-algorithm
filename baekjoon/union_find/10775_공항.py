import sys
sys.setrecursionlimit(10**6)
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

g = []
parent = [i for i in range(G+1)]
for _ in range(P):
    g.append(int(sys.stdin.readline()))


def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    parent[a] = b

cnt = 0
for i in g:
    v = find(i)
    if v == 0:
        break

    union(v, v-1)
    cnt += 1

print(cnt)

# 이중 for문으로는 시간복잡도 높아서 안풀림
# 유니온 파운드로 풀어야
# 시간복잡도 계산하고 푸는 습관이 필요함....
# import sys
# G = int(sys.stdin.readline())
# P = int(sys.stdin.readline())
#
# g = []
# for _ in range(P):
#     g.append(int(sys.stdin.readline()))
#
# result = [0] * (G+1)
# cnt = 0
# for i, v in enumerate(g):
#     if result[v] == 0:
#         result[v] = v
#         cnt += 1
#         continue
#
#     flag = False
#     for j in range(1, v+1):
#         if result[j] == 0:
#             flag = True
#             result[j] = v
#             cnt += 1
#             break
#
#     if not flag:
#         print(cnt)
#         sys.exit()
#
# print(cnt)
