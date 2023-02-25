import sys
n = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
cnt = 0

for i in boxes:
    if cranes[0] < i:
        print(-1)
        break
else:
    while boxes:
        if not boxes:
            break

        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        cnt += 1

    print(cnt)

