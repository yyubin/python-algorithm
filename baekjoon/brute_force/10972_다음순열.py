import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
for i in range(n-1, 0, -1):
    if li[i-1] < li[i]:
        for j in range(n-1, 0, -1):
            if li[i-1] < li[j]:
                li[i-1], li[j] = li[j], li[i-1]
                li = li[:i] + sorted(li[i:])
                print(*li)
                sys.exit()
print(-1)

# 1 4 3 2의 경우
# 뒤에서부터 뒷 값이 앞 값보다 큰 경우까지 반복
# 3, 2는 해당 안됨, 4 3 도 해당안됨 1 4가 해당됨
# 이때 1의 인젝스를 x로 두고
# 4의 인덱스를 y라 하자

# 다시 뒤에서부터 값을 비교하며 인덱스 x보다 큰 값이 있으면 바꿈
# 1 2 비교가 되고 2가 크기 때문에 1 2 자리가 바뀜 2 4 3 1

# y에 해당하는 인덱스부터 sort 오름차순을 한 뒤 이어붙임
# 4 3 1 sort 하여 1 3 4가 되고
# 이어 붙이면 2 1 3 4 가 됨

## c++엔 next permutation 함수가 이미 있는데 이와 같은 방식임


# 시간초과
# permutations 시간복잡도 o(n!) zzz

# import sys
# from itertools import permutations
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# tu = tuple(li)
# li.sort()
#
# flag = False
# for i in permutations(li, n):
#     if flag:
#         print(*i)
#         sys.exit()
#     if i == tu:
#         flag = True
#
# print(-1)
