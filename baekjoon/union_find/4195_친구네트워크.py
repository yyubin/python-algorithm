import sys
sys.setrecursionlimit(10 ** 6)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_ = find(a)
    b_ = find(b)

    if a_ != b_:
        parent[b_] = a_
        num[a_] += num[b_]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    parent = dict()
    num = dict()
    for _ in range(n):
        x, y = map(str, sys.stdin.readline().split())

        if x not in parent:
            parent[x] = x
            num[x] = 1
        if y not in parent:
            parent[y] = y
            num[y] = 1

        union(x, y)
        print(num[find(x)])


## https://wondev.tistory.com/205
# 아이디어가 생각이 안남 ㅜ


# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

## 부모 노드들을 최적화하지 않음
# 트리 깊어질 경우 효율 낮아짐

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
# 경로 압축 적용한 버전
# 재귀적으로 루트노드 찾으면서 현재 노드부터 루트 노드 사이에 있는 모든 노드의 부모를 루트 노드로 설정


