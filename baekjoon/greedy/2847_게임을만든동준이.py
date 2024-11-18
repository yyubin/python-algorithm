import sys
n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]
score.reverse()
cnt = 0
for i in range(n-1):
    if score[i] <= score[i+1]:
        tmp = score[i+1]
        score[i+1] = score[i] - 1
        cnt += abs(tmp - score[i+1])
print(cnt)
