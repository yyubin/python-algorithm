import sys
from collections import defaultdict
from string import ascii_lowercase
s = sys.stdin.readline().rstrip()
d = defaultdict(int)
alphabet_list = list(ascii_lowercase)
for ch in s:
    d[ch] += 1
for ch in alphabet_list:
    print(d[ch], end=' ')
