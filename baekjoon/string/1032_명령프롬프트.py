import sys
n = int(sys.stdin.readline())
li = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

result = li[0]
li.pop(0)

for i in li:
    for j in range(len(result)):
        if result[j] != i[j]:
            result[j] = '?'


print(*result, sep="")
