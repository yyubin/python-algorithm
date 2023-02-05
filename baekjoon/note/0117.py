#1085
# x, y, w, h = map(int, input().split())
#
# x_ = min(abs(w-x), abs(0-x))
# y_ = min(abs(h-y), abs(0-y))
#
# print(min(x_, y_))

#1259
# while True:
#     string = input()
#     if string == '0':
#         break
#
#     string = list(map(int, string))
#     print('yes' if string == string[::-1] else 'no')

#10828번 스택
# import sys
# cnt = int(sys.stdin.readline())
# stack = []
#
# while cnt > 0:
#     li = list(sys.stdin.readline().rstrip().split())
#
#     if li[0] == 'push':
#         stack.append(li[1])
#     elif li[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif li[0] == 'size':
#         print(len(stack))
#     elif li[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif li[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[len(stack) - 1])
#
#     cnt -= 1


#11650 좌표 정렬하기
# import sys
# n = int(sys.stdin.readline())
# li = []
#
# for _ in range(n):
#     li.append(list(map(int, sys.stdin.readline().split())))
#
# li.sort()
# for i in li:
#     print(i[0], i[1])


#10845 큐
# import sys
# cnt = int(sys.stdin.readline())
# q = []
#
# while cnt > 0:
#     li = list(sys.stdin.readline().rstrip().split())
#
#     if li[0] == 'push':
#         q.append(li[1])
#     elif li[0] == 'pop':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.pop(0))
#     elif li[0] == 'size':
#         print(len(q))
#     elif li[0] == 'empty':
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     elif li[0] == 'front':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
#     elif li[0] == 'back':
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[len(q) - 1])
#
#     cnt -= 1

#11651번 좌표정렬하기2
# import sys
# n = int(sys.stdin.readline())
# li = []
#
# for _ in range(n):
#     li.append(list(map(int, sys.stdin.readline().split())))
#
# li = sorted(li, key=lambda x: (x[1], x[0]))
# for i in li:
#     print(i[0], i[1])

#1181번 단어 정렬
# import sys
# n = int(sys.stdin.readline())
# li = []
#
# for _ in range(n):
#     li.append(sys.stdin.readline().rstrip())
#
# li = set(li)
# li = sorted(li, key=lambda x: (len(x), x))
#
# print(*li, sep="\n")


#10866 덱
# import sys
# from collections import deque
# cnt = int(sys.stdin.readline())
# dq = deque([])
#
# while cnt > 0:
#     li = list(sys.stdin.readline().rstrip().split())
#
#     if li[0] == 'push_front':
#         dq.appendleft(li[1])
#     elif li[0] == 'push_back':
#         dq.append(li[1])
#     elif li[0] == 'pop_front':
#         if len(dq) == 0:
#             print(-1)
#         else:
#             print(dq.popleft())
#     elif li[0] == 'pop_back':
#         if len(dq) == 0:
#             print(-1)
#         else:
#             print(dq.pop())
#     elif li[0] == 'size':
#         print(len(dq))
#     elif li[0] == 'empty':
#         if len(dq) == 0:
#             print(1)
#         else:
#             print(0)
#     elif li[0] == 'front':
#         if len(dq) == 0:
#             print(-1)
#         else:
#             print(dq[0])
#     elif li[0] == 'back':
#         if len(dq) == 0:
#             print(-1)
#         else:
#             print(dq[len(dq) - 1])
#
#     cnt -= 1

#2164번 카드2
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# cards = deque([i+1 for i in range(n)])
#
# while len(cards) != 1:
#     cards.popleft()
#     tmp = cards.popleft()
#     cards.append(tmp)
#
# print(cards[0])

#10816번 숫자 카드2
# import sys
# n = int(sys.stdin.readline())
# li1 = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# li2 = list(map(int, sys.stdin.readline().split()))
#
# result = [0] * m
# for i, v in enumerate(li2):
#     for j in li2:
#         if v == j:
#             result[i] += 1
#
# print(*result, sep=" ")

# from sys import stdin
# from collections import Counter
# _ = stdin.readline()
# N = stdin.readline().split()
# _ = stdin.readline()
# M = stdin.readline().split()
#
# C = Counter(N)
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M))

#2609
# import math
# import sys
# a, b = map(int, sys.stdin.readline().split())
#
# print(math.gcd(a, b))
# print(math.lcm(a, b))

#11050 이항계수
#nCk -> factorial(n)//(factorial(k)*factorial(n-k))
# import sys
#
# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)
#
# n, k = map(int, sys.stdin.readline().split())
# print(fac(n)//(fac(k)*fac(n-k)))

#2798
import sys
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            result.append(li[i] + li[j] + li[k])

result.sort(reverse=True)
for i in result:
    if i <= m:
        print(i)
        break

