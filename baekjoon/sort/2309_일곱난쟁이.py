import sys
li = [int(sys.stdin.readline()) for _ in range(9)]

remain = sum(li) - 100

for i in li:
    if (remain - i) in li and remain-i != i:
        li.pop(li.index(remain-i))
        li.pop(li.index(i))
        break

li.sort()
print(*li, sep='\n')
