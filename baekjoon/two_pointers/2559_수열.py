import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

now = sum(li[:k])
ans = now

for i in range(k, n):
    now = now + li[i] - li[i-k]
    ans = max(now, ans)

print(ans)

# 예제는 맞는데 뭐가 틀렸지? ㅜㅜ
# import sys
# n, k = map(int, sys.stdin.readline().split())
# li = list(map(int, sys.stdin.readline().split()))
#
# start = 0
# end = len(li) - 1
#
# while end - start >= k:
#     if li[start] < li[end]:
#         start += 1
#     else:
#         end -= 1
#
# sum_ = sum(li[start:end+1])
# print(sum_)
#
