## 2023 kakao blind
# greedy + dfs

import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)

    if dist > k or (k - dist) % 2 != 0:
        return "impossible"

    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    answer = ''

    def dfs(curr_x, curr_y, path, count):
        nonlocal answer
        if answer != "":
            return

        remain_dist = abs(curr_x - r) + abs(curr_y - c)
        if remain_dist > k - count:
            return

        if count == k:
            if curr_x == r and curr_y == c:
                answer = path
            return

        for char, dx, dy in directions:
            nx, ny = curr_x + dx, curr_y + dy
            if 1 <= nx <= n and 1 <= ny <= m:
                dfs(nx, ny, path + char, count + 1)
                if answer != "":
                    return

    dfs(x, y, "", 0)
    return answer if answer else "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
