from collections import deque, defaultdict

def solution(begin, target, words):
    q = deque([(begin, 0)])
    n = len(words[0])
    visited = defaultdict(bool)

    if begin in words:
        visited[begin] = True

    while q:
        now, cnt = q.popleft()

        if now == target:
            return cnt

        for w in words:
            tmp = 0
            for i in range(n):
                if w[i] == now[i]:
                    tmp += 1
            if tmp == n-1 and not visited[w]:
                q.append((w, cnt+1))
                visited[w] = True

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))