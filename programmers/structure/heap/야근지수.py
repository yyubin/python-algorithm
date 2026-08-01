import heapq
def solution(n, works):
    pq = [-1 * i for i in works]
    heapq.heapify(pq)

    for _ in range(n):
        now = heapq.heappop(pq)
        heapq.heappush(pq, now + 1)

    answer = 0
    pq = [-1 * i for i in pq]
    for i in pq:
        if i > 0:
            answer += i * i

    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))