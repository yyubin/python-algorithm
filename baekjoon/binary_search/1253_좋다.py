import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li.sort()
result = []

for i in range(len(li)):
    start = 0
    end = len(li) - 1

    while start < end:
        if end == i:
            end -= 1
            continue
        elif start == i:
            start += 1
            continue

        tmp = li[end] + li[start]

        if tmp == li[i]:
            result.append(li[i])
            break
        elif tmp > li[i]:
            end -= 1
        else:
            start += 1

print(len(result))