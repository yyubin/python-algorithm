# 12865번 평범한 배낭 -> 다이나믹
# n, k = map(int, input().split())
# objects = []
#
# for i in range(n):
#     objects.append(list(map(int, input().split())))
#
# s = [0]*(n+1)
#
# for i in objects:
#     sm = i[0]
#     satis = i[1]
#     for j in objects:
#         if sm + j[0] > k:
#             s.append(satis)
#         else:
#             sm += j[0]
#             satis += j[1]
#
# print(max(s))

# N, K = map(int, input().split())
#
# sum_value = [[0]*(K+1) for i in range(N+1)]
# W = [0]*(N+1)
# V = [0]*(N+1)
#
# for i in range(1, N+1):
#     W[i], V[i] = map(int, input().split())
#
#     for j in range(1, K+1):
#         if W[i] > j: #현재 무게가 j보다 크면
#             sum_value[i][j] = sum_value[i-1][j] #해당 테이블에 이전단계 만족도 넣기
#         else:
#             sum_value[i][j] = max(sum_value[i-1][j], V[i]+sum_value[i-1][j-W[i]]) # 이전단게 만족도와 지금 현재 단계에 만족도 더한값 중 더 큰 값
#
# print(sum_value[N][K])

# 2579번 : 계단오르기
# n = int(input())
#
# N = [[0] for i in range(n+1)]
# S = [0]*(n+1)
#
# for i in range(1, n+1):
#     S[i] = int(input())
#
#     for j in range(1, n+1):
#         if S[i] > j:

# 1475번 : 방번호
# num = list(map(int, input()))
# num = [6 if i == 6 or i == 9 else i for i in num]
#
# li = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8]
# cnt = 1
#
# for i in num:
#     if i in li:
#         li.remove(i)
#     else:
#         cnt += 1
#         li += [0, 1, 2, 3, 4, 5, 6, 6, 7, 8]
#         li.remove(i)
#
# print(cnt)

# 10819번 : 차이를 최대로
# n = int(input())
# li = list(map(int, input().split()))
#
# result = 0
#
# while len(li) > 1:
#     result += max(abs(max(li) - min(li)), abs(min(li) - max(li)))
#     print(result)
#     li.remove(max(li))
#     li.remove(min(li))
#
# if len(li) == 1:
#     result += max(li)
#
# print(result)

# 2525번 : 오븐시계
# h, m = map(int, input().split())
# tm = int(input())
#
# m += tm
#
# while m > 59:
#     h += 1
#     m -= 60
#     if h > 23:
#         h = 0
#
# print(h, m)

#1008번
# a, b = map(int, input().split())
# print(a/b)

#2751번 : 수정렬
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

li.sort()
print(*li, sep="\n")
