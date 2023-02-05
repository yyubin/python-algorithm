import sys
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

r, g, b = [0]*n, [0]*n, [0]*n
r[0] = li[0][0]
g[0] = li[0][1]
b[0] = li[0][2]

for i in range(1, n):
    r[i] = min(g[i-1], b[i-1]) + li[i][0]
    g[i] = min(r[i-1], b[i-1]) + li[i][1]
    b[i] = min(r[i-1], g[i-1]) + li[i][2]

print(min(r[n-1], g[n-1], b[n-1]))



# 내가 생각한대로 구현하긴 했는데, 모든 경우에서의 최솟값을 구하려면 dp써야할듯 ㅎ하하핳ㅎㅎ
# result = []
# pre = n
# for i, v in enumerate(li):
#     if v.index(min(v)) != pre:
#         result.append(min(v))
#         pre = v.index(min(v))
#         continue
#     v[v.index(min(v))] = 1001
#     result.append(min(v))
#     pre = v.index(min(v))
#
# print(sum(result))
