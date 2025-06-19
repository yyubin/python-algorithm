import sys
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

essential = {'a', 't', 'n', 'i', 'c'}
if k < 5:
    print(0)
    sys.exit()

word_mask = []
for w in words:
    mask = 0
    for ch in set(w):
        mask |= (1 << ord(ch) - ord('a'))
    word_mask.append(mask)

ess_mask = 0
for w in essential:
    ess_mask |= (1 << ord(w) - ord('a'))

candidates = [chr(i+ord('a')) for i in range(26) if chr(i+ord('a')) not in essential]
res = 0

for comb in combinations(candidates, k-5):
    teach = ess_mask
    for ch in comb:
        teach |= (1 << ord(ch) - ord('a'))

    tmp = 0
    for w_mask in word_mask:
        if (teach & w_mask) == w_mask:
            tmp += 1

    res = max(tmp, res)

print(res)
