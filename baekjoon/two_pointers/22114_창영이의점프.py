import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

res = 1
left = 0
jump = 0

for right in range(n-1):
    if li[right] > k:
        jump += 1

    while jump > 1:
        if li[left] > k:
            jump -= 1
        left += 1

    res = max(res, right - left + 2)
print(res)

# d = [[0, 0] for _ in range(n)]
# d[0][0] = 1
# used = False
#
# start = 0
# for i in range(n-1):
#
#
# for i in range(n-1):
#     if li[i] <= k:
#         d[i+1][0] = max(d[i][0]+1, d[i][1]+1)
#     else:
#         if not used:
#             used = True
#             d[i+1][1] = d[i][0] + 1
#         else:
#             print(i+1)
#             sys.exit()
#     print(d)
# print(max(d[-1]))
