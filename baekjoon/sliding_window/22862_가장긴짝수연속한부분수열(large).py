import sys
n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
left = 0
odd = 0
res = 0
for right in range(n):
    if s[right] % 2 == 1:
        odd += 1
    while odd > k:
        if s[left] % 2 == 1:
            odd -= 1
        left += 1
    res = max(res, right - left + 1 - odd)
print(res)

# 수열에서 최대 k개의 홀수 삭제 가능
# 짝수로만 이루어진 가장 긴 연속 부분 수열
# 윈도우는 left, right로 정의 -> 가변 길이 윈도우
# odd가 k보다 커지면 홀수가 빠질때까지 left += 1

# 현재 윈도우 길이에서 (right-left+1) 홀수 개수를 뺀 것이 최선의 값
