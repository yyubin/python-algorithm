# 10815번 숫자카드
# import sys
# n = int(sys.stdin.readline())
# li_n = list(map(int, sys.stdin.readline().split()))
#
# m = int(sys.stdin.readline())
# li_m = list(map(int, sys.stdin.readline().split()))
#
# li = [1 if i in li_n else 0 for i in li_m]
# print(li)

# import sys
#
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))
#
# _dict = {}  # 속도는 dictionary!
# for i in range(len(cards)):
#     _dict[cards[i]] = 0  # 아무 숫자로 mapping
#
# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')

# 리스트 컴프리헨션이 더 간결한데 왜 속도는 딕셔너리가 빠를까..?


# 2470번 두 용액
# import sys
#
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
#
# li.sort()
# print(li)
# start = 0
# end = len(li) - 1
#
# result = 0
# while start <= end:
#     mid = (start + end) // 2
#     print("최초", start, end, mid)
#     if (li[start] + li[end]) == 0:
#         print(li[start], li[end], sep=" ")
#         break
#     elif (li[start] + li[end]) > 0:
#         print(li[start] + li[end])
#         end = mid - 1
#
#         print("감소 시켜야 함", start, end)
#     else:
#         print(li[start] + li[end])
#         start = mid + 1
#         print("증가 시켜야함", start, end)
#
# print(start, end)
# print(li[start], li[end], sep=" ")

# 투포인터로 풀어보기
import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

left = 0
right = n - 1

result = []
temp = []

while left < right:
    m = li[left] + li[right]
    if m == 0:
        result = [[li[left], li[right]]]
        break
    else:
        result.append([li[left], li[right]])
        temp.append(m)

        if m > 0:
            right -= 1
        else:
            left += 1

if len(result) == 1:
    print(*result[0], sep=" ")
else:
    temp = [abs(i) for i in temp]
    print(*result[temp.index(min(temp))], sep=" ")

## 대다내~


# 2588번
n = int(input())
m = input()
li = list(m)

for i in li[::-1]:
    print(n*int(i))
print(n*int(m))
