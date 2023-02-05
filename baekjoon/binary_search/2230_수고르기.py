import sys

n, m = map(int, sys.stdin.readline().split())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))
li.sort()

start = 0
end = 1

result = sys.maxsize

while start < n and end < n:
    tmp = li[end] - li[start]
    if tmp > m:
        result = min(tmp, result)
        start += 1
    elif tmp == m:
        result = tmp
        break
    else:
        end += 1

print(result)
# 차이 구해야 하는데 시발 지금까지 더하고 있었음..


# import sys
#
# input = sys.stdin.readline
# INF = sys.maxsize
#
# def solve():
#     left, right = 0, 1
#
#     result = INF
#     while left < n and right < n:
#         tmp = arr[right] - arr[left]
#         if tmp == m:
#             print(tmp)
#             exit(0)
#         elif tmp > m:
#             result = min(result, tmp)
#             left += 1
#         else:
#             right += 1
#
#     return result
#
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# arr.sort()
# print(solve())