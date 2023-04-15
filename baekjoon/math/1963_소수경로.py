import sys
from collections import deque
def find_prime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs():
    q = deque()
    q.append((start, 0))

    visited = [0 for _ in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        str_now = str(now)

        if now == end:
            return cnt

        for i in range(4):
            for j in range(10):
                tmp = int(str_now[:i] + str(j) + str_now[i+1:])

                if visited[tmp] == 0 and prime[tmp] and tmp >= 1000:
                    visited[tmp] = 1
                    q.append((tmp, cnt+1))


tc = int(sys.stdin.readline())
prime = [True for _ in range(10000)]
find_prime()

for _ in range(tc):
    start, end = map(int, sys.stdin.readline().split())
    print(bfs())


## bfs로 풀어야한다는 생각이 안든다..;



