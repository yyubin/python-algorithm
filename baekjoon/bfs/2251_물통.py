from collections import deque
import sys
A, B, C = map(int, sys.stdin.readline().split())
visited = [[False] * (B + 1) for _ in range(A + 1)]
answer = set()

def pour(a, b, c, from_idx, to_idx, limits):
    state = [a, b, c]
    from_amt = state[from_idx]
    to_amt = state[to_idx]

    move = min(from_amt, limits[to_idx] - to_amt)
    state[from_idx] -= move
    state[to_idx] += move

    return tuple(state)

def bfs():
    q = deque()
    q.append((0, 0, C))
    visited[0][0] = True

    while q:
        a, b, c = q.popleft()
        if a == 0:
            answer.add(c)

        limits = [A, B, C]
        for from_idx, to_idx in [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]:
            na, nb, nc = pour(a, b, c, from_idx, to_idx, limits)
            if not visited[na][nb]:
                visited[na][nb] = True
                q.append((na, nb, nc))

bfs()
print(*sorted(answer))
