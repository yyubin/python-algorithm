# 2606번: 바이러스
computer = int(input())
line = int(input())
li = []

for i in range(line):
    x, y = map(int, input().split())

    for j in range(len(li)):
        if x in j:
            li[j].append(x)


    if x not in li:
        li2 = [x, y]
        li.append(li2)

    else:
        for i in range(len(li)):
            pass

