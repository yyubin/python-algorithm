import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
x, y = 0, float('inf')
for i in range(1, n, 2):
    x = x + li[i] - li[i - 1]
    y = min(x, y) + li[i + 1] - li[i]
print(y)

# 기본적으로 정렬 후 2명씩 짝지으며 어색함 누적합을 구하고 (x),
# 중간에 한 번만 3명을 묶었을 때 최소 어색함 합이 되는 지점을 찾아서 (y)
# 최종적으로 그 중 가장 작은 합을 출력하는 방식tq