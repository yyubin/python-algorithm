n = int(input())
if n%2 == 0:
    print('CY')
else:
    print('SK')

# d[1] = 1
# d[2] = 2
# d[3] = 1
#
# for i in range (4, n+1):
#     d[i] = min(d[i-1], d[i-3]) + 1
#
# if d[n]%2 == 1:
#     print('SK')
# else:
#     print('CY')

# d[n] 에서 n은 돌이 n개 일때 턴의 개수
# d[1] = 1
# d[2] = 2
# d[3] = 1
# d[4]에서 돌은 1개 또는 3개를 가져갈 수 있음
# 턴의 개수를 최소로 해야함
# d[4] = min(d[4-1], d[4-3]) + 1

# 1: SK(1) :: SK
# 2: SK(1), CY(1) :: CY
# 3: SK(3) :: SK
# 4: SK(1), CY(3) :: CY
#  : SK(3), CY(1) :: CY
# 5: SK(1), CY(3), SK(1) :: SK
#  : SK(3), CY(1), SK(1) :: SK
# 6: SK(1), CY(1), SK(1), CY(3) :: CY
#  : SK(1), CY(1), SK(3), CY(1) :: CY
