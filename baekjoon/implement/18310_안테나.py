import sys
n = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()
print(houses[(n-1)//2])

# 절댓값 거리의 합이 최소가 되는 지점은 중앙값
