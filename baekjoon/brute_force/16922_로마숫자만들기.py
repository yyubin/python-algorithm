import sys
from itertools import combinations_with_replacement
n = int(sys.stdin.readline())
st = [1, 5, 10, 50]
nums = []
for i in combinations_with_replacement(st, n):
    tmp = sum(i)
    if tmp not in nums:
        nums.append(tmp)
print(len(nums))

# set 쓰면 더 빠를듯
