import sys
cnt = int(sys.stdin.readline())
li = []
for _ in range(cnt):
    num = int(sys.stdin.readline())
    if num == 0:
        li.pop()
    else:
        li.append(num)

print(sum(li))
