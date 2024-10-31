import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 0
end = k

while start <= end:
    mid = (start+end)//2
    tmp = 0

    for i in range(1, n+1):
        tmp += min(mid//i, n)

    if tmp < k:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)


## mid는 현재값
## start = 0, end = k
## 가능한 값이 0부터 k까지

## mid//i
# 지금의 i행에서 지금 mid보다 작은게 몇개있는지 세는 것

# 예를들어 i가 2일이고 mid가 6이라면
# 2번째 행에서 6보다 작은게 몇개 있는지 세는 것
# 6//2 = 3인데, 이는 2, 3, 6이된다. 이 세개가 mid보다 이하인 값이고
# 갯수를 리턴한다

# min으로 n을 두는건 최댓값이 n이기 때문(그니ㅏㄲ 한행이 전부다 mid보다 작은수라고 해도 행자체가 최대 n개라서)

# 그래서 이 개수를 모두 세서 가능한 개수를 찾았는데 이게 k보다 작은 경우는
# k번째에 도달하지 못했다는 것


# 저걸 mid//i로 구해야겠다는 생각이 안남...; ㅜㅜ

## 시간초과에서는
# start += 1 이런식으로 해서 범위 좁힐때 실수함



## 3x3
#   1 2 3
# 1 1 2 3
# 2 2 4 6
# 3 3 6 9
# 1 2 2 3 3 4 6 6 9
