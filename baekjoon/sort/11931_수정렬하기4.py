import sys
n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort(reverse=True)
print(*nums, sep='\n')
