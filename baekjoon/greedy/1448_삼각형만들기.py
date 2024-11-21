import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort(reverse=True)

for i in range(n-2):
    hypo = li[i]
    if li[i+1] + li[i+2] > hypo:
        print(hypo + li[i+1] + li[i+2])
        sys.exit()

print(-1)


