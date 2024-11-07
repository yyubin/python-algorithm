import sys
n, m, l = map(int, sys.stdin.readline().split())
li = [0] + list(map(int, sys.stdin.readline().split())) + [l]
start, end, result = 1, l-1, 0
li.sort()

while start <= end:
    mid = (start+end) // 2

    tmp = 0
    for i in range(1, len(li)):
        if li[i] - li[i-1] > mid:
            tmp += (li[i]-li[i-1]-1)//mid

    if tmp > m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)
# mid = 휴게소 간격
# tmp += (li[i]-li[i-1]-1)//mid
# 현재 이미 설치된 곳은 설치 불가능하니까 1빼주는 것

