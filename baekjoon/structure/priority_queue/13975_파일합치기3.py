import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(li)

    res = 0

    while len(li) >= 2:
        tmp1 = heapq.heappop(li)
        tmp2 = heapq.heappop(li)

        tmp = tmp1 + tmp2

        res += tmp
        heapq.heappush(li, tmp)

    print(res)

# 우선순위 큐 사용 -> heapq 사용
# 총 N - 1의 합병 필요, 매번 heappop 2번, heappush 1번 수행, heapify 한번 수행
# O(log N) 연산을 매 연산마다 3번 수행, O(3 log N) N-1번 반복시

## 시간복잡도 : O(N log N)