import sys
cycle = int(sys.stdin.readline())

while cycle != 0:

    num = int(sys.stdin.readline())
    heap = []

    for _ in range(num):
        heap.append(list(map(int, sys.stdin.readline().split())))

    heap.sort()
    a, b = heap[0][0], heap[0][1]
    cnt = 1
    for i in range(0, len(heap)):
        if a > heap[i][0] or b > heap[i][1]:
            a = heap[i][0]
            b = heap[i][1]
            cnt += 1

    print(cnt)
    cycle -= 1
