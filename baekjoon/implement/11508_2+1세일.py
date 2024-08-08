import sys

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort(reverse=True)
result = 0

while len(li) >= 3:
    result += li.pop(0)
    result += li.pop(0)
    li.pop(0)

if li:
    result += sum(li)

print(result)
