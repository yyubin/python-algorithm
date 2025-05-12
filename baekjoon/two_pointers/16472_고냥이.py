import sys
from collections import defaultdict
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

left = 0
right = 0
max_len = 0
counter = defaultdict(int)

while right < len(s):
    counter[s[right]] += 1
    right += 1

    while len(counter) > n:
        counter[s[left]] -= 1
        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1

    max_len = max(max_len, right - left)
print(max_len)