import sys
n = int(sys.stdin.readline())
li1 = []
li2 = []
result = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp == 1:
        result += 1
    elif tmp > 0:
        li1.append(tmp)
    else:
        li2.append(tmp)

li1.sort()
li2.sort(reverse=True)

while len(li1) != 0:
    if len(li1) == 1:
        result += li1.pop()
    else:
        result += li1.pop() * li1.pop()

while len(li2) != 0:
    if len(li2) == 1:
        result += li2.pop()
    else:
        result += li2.pop() * li2.pop()

print(result)
