import sys
sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())
def find_parent_and_depth(node, parent, depth):
    depth_arr[node] = depth
    parent_arr[node] = parent
    for child in tree.get(node, []):
        if child != parent:
            find_parent_and_depth(child, node, depth + 1)

def lca(a, b):
    while depth_arr[a] > depth_arr[b]:
        a = parent_arr[a]
    while depth_arr[b] > depth_arr[a]:
        b = parent_arr[b]
    while a != b:
        a = parent_arr[a]
        b = parent_arr[b]
    return a

for _ in range(t):
    n = int(sys.stdin.readline())
    parent_arr = [0] * (n + 1)
    depth_arr = [0] * (n + 1)
    tree = dict()
    is_child = [False] * (n + 1)

    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        tree.setdefault(a, []).append(b)
        tree.setdefault(b, []).append(a)
        is_child[b] = True

    root = is_child.index(False, 1)
    find_parent_and_depth(root, 0, 0)
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))

