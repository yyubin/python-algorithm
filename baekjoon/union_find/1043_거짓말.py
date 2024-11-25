import sys
n, m = map(int, sys.stdin.readline().split())
people = list(map(int, sys.stdin.readline().split()))
truth = set(people[1:])
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


party = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
cnt = m
for i in range(m):
    li = party[i][1:]
    p = li[0]
    for j in range(1, len(li)):
        if find(p) != find(li[j]):
            union(p, li[j])

visited = [0] * (n+1)
for i in range(1, n+1):
    if i in truth and not visited[i]:
        p = find(i)
        for j in range(1, n+1):
            if find(j) == p:
                visited[j] = 1
                truth.add(j)

for i in range(m):
    for j in range(1, party[i][0] + 1):
        if party[i][j] in truth:
            cnt -= 1
            break

print(cnt)


# 입력받은 값 같은 파티참석하는 경우 그룹으로 묶음
# 진실을 아는 사람의 부모를 찾고
# 사람들 순회하면서 부모가 같은 경우 방문 표시후 아는 사람 리스트에 추가
# 파티 다시 순회하면서 아는사람 리스트에 포함된 사람이 있다면 cnt -= 1
# 한명이라도 찾으면 break 걸어서 중복 count 안됨



