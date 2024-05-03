# TRIE
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for c in string:
            if c not in cur_node.children:
                cur_node.children[c] = Node(c)
            cur_node = cur_node.children[c]


def print_(now, i, isHead=False):
    if not isHead:
        print('--' * i + now.key)
    sorted_keys = sorted(now.children.keys())
    for child in sorted_keys:
        print_(now.children[child], i + 1)


n = int(sys.stdin.readline())
trie = Trie()
for _ in range(n):
    tmp = sys.stdin.readline().split()[1:]
    trie.insert(tmp)

print_(trie.head, -1, True)

## 그냥 구현
import sys
n = int(input())
food = []
for _ in range(n):
    tmp = list(map(str, sys.stdin.readline().split()))
    food.append(tmp[1:])

food.sort()

result = []
for i in range(n):
    if i == 0:
        for j in range(len(food[i])):
            result.append('--'*j+food[i][j])
    else:
        idx = 0
        for j in range(len(food[i])):
            if len(food[i-1]) <= j or food[i-1][j] != food[i][j]:
                break
            else:
                idx = j+1
        for j in range(idx, len(food[i])):
            result.append('--'*j+food[i][j])

print(*result, sep="\n")


# import sys
# n = int(sys.stdin.readline())
# graph = []
# owner = []
# chk = []
#
# for x in range(n):
#     tmp = list(map(str, sys.stdin.readline().split()))
#     k = int(tmp.pop(0))
#
#     if tmp[0] not in owner:
#         owner.append(tmp[0])
#
#     tmp_owner = tmp[0]
#     tmp_ser = []
#     for i in range(1, k):
#         if (tmp_owner, tmp[i], i) not in chk:
#             tmp_ser.append((tmp_owner, tmp[i], i, x))
#             chk.append((tmp_owner, tmp[i], i))
#
#     graph.append(tmp_ser)
#
# graph.sort()
# owner.sort()
#
# for own in owner:
#     print(own)
#     for ser in graph:
#         for se in ser:
#             if own == se[0]:
#                 print('--' * se[2], end="")
#                 print(se[1])


# 주인
# 단계
# 하인

# A C
# 주인 A 하인 C 단계 1

# A B C D
# 주인 A 하인 B 단계 1
# 주인 A 하인 C 단계 2
# 주인 A 하인 D 단계 3
