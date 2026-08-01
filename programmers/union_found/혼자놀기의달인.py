def solution(cards):
    cards = [0] + cards
    visited = [0] * len(cards)
    idx = 1

    def parent_check(parent, now):
        visited[now] = parent

        if visited[cards[now]] == 0:
            parent_check(parent, cards[now])

    for i in range(1, len(cards)):
        if visited[i] == 0:
            parent_check(idx, i)
            idx += 1

    if max(visited) == 1:
        return 0

    li = []
    for c in range(1, max(visited)+1):
        li.append(visited.count(c))
    li.sort()
    return li[-1] * li[-2]

print(solution([8,6,3,7,2,5,1,4]))
print(solution([1, 2]))
print(solution([2, 1]))