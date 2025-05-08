import sys
g = int(sys.stdin.readline())
res = []

start = 1
end = 2
while start < end:
    diff = end**2 - start**2
    if diff == g:
        res.append(end)
        end += 1
    elif diff < g:
        end += 1
    else:
        start += 1

if res:
    print(*res, sep="\n")
else:
    print(-1)

# end^2 - start^2 = G
# 이때 start가 증가하면 diff는 감소, end가 증가하면 diff는 증가
# end^2 - start^2 > G이면 start += 1
# end^2 - start^2 < G이면 end += 1
# 반복 조건은 start < end일 때까지만

# 투포인터 사용처
# 1. 정렬된 배열
# 2. 두 수의 차이, 합 등 특정한 관계를 만족하는 쌍을 찾을때
#       위 문제가 해당
# 3. 길이가 고정되거나 가변적인 "연속 구간"을 찾을 때
#       최솟값, 부분합 문제에서 사용
# 4. 두 리스트를 동시에 스캔하며 병합하거나 비교 할 때
#       같은 원소 찾기, 두 배열 비교 등