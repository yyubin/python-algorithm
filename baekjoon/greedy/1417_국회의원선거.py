import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)] + [0]
now = li.pop(0)
li.sort(reverse=True)
cnt = 0

while max(li) >= now:
    if max(li) == li[0]:
        cnt += 1
        now += 1
        li[0] -= 1
    else:
        li.sort(reverse=True)

print(cnt)
