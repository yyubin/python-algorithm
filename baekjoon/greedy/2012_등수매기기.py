import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()
score = 0
for i, v in enumerate(li):
    score += abs((i+1) - v)

print(score)