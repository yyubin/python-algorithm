import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = [0] * n
res = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]

    d[i] += 1

print(max(d))

tmp = []
order = max(d)
for i in range(n-1, -1, -1):
    if d[i] == order:
        tmp.append(a[i])
        order -= 1

tmp.reverse()
print(*tmp)


## 이분탐색 풀이
# import sys
# from bisect import bisect_left
# input = sys.stdin.readline
#
# N = int(input())
# List = list(map(int, input().split()))
# Ans = [], Index = []
# Length = 0
#
# for num in List:
#     if not Ans or Ans[-1]<num:
#         Ans.append(num)
#         Index.append(Length)
#         Length += 1
#     else:
#         Temp = bisect_left(Ans,num)
#         Ans[Temp] = num
#         Index.append(Temp)
#
# print(Length)
# Temp = []
# for i in range(N-1, -1, -1):
#     if Index[i] == Length-1:
#         Temp.append(List[i])
#         Length -= 1
# print(*Temp[::-1])
