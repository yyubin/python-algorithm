import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
d = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i-j] + li[j-1], d[i])

print(d[n])

## dp 였음
# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# cards = []
#
# for i in range(n):
#     cards.append((i+1, li[i], li[i]/(i+1)))
#
# cards.sort(key= lambda x: (-x[2], -x[1]))
# get = n
# res = 0
# for i in range(n):
#     if get%cards[i][0] == 0:
#         res += cards[i][1] * (get//cards[i][0])
#         break
#     else:
#         res += cards[i][1] * (get//cards[i][0])
#         get %= cards[i][0]
# print(res)
#
#
