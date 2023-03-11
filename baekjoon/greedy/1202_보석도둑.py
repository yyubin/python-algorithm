import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
jewels = []
bags = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    jewels.append((a, b))

for _ in range(k):
    bags.append(int(sys.stdin.readline()))

jewels.sort()
bags.sort()

tmp = []
result = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]: #첫번째 보석을 가방에 넣을 수 있으면
        heapq.heappush(tmp, -jewels[0][1]) #보석 가방에 넣고 값은 tmp에 저장
        heapq.heappop(jewels)

    if tmp: # tmp돌면서
        result += heapq.heappop(tmp) # 결과 pop한 후 더해주기
    elif not jewels: #보석 없으면 종료
        break

print(-result)
# python heapq는 min heap 이기 때문에 pop하면 최소 값을 주게 됨
# 여기에서 최댓값을 구해야 하기 때문에 tmp에 jewels 넣을때 - 붙여서 넣어줌
# 프린트할 땐 다시 - 붙여서 출력하면 최댓값 내줌


# 우선순위 큐
# https://heytech.tistory.com/68

# 시간 초과
# jewels.sort(key=lambda x: -x[1])
# bags.sort()

# result = []
# for i in range(n):
#     for j in range(k):
#         if jewels[i][0] <= bags[j]:
#             result.append(jewels[i][1])
# print(sum(result))
