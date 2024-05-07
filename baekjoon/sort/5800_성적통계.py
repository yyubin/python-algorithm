import sys
k = int(sys.stdin.readline())

for i in range(k):
    li = list(map(int, sys.stdin.readline().split()))
    n = li.pop(0)
    li.sort()
    gap = 0
    for j in range(1, n):
        gap = max(gap, li[j]-li[j-1])
    print(f'Class {i+1}')
    print(f'Max {max(li)}, Min {min(li)}, Largest gap {gap}')

